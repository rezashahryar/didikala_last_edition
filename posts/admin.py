from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Tag, Category
# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ['title', 'status']
    prepopulated_fields = {'slug': ('title',)}
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
