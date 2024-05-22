from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Tag
# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ['title']
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
