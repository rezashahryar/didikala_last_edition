from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'sub_category', 'price', 'inventory', 'available']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.ProductCategory)
class ProductCategory(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.ProductProperties)
class ProductPropertiesAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(models.SubProductCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'main_category']
    prepopulated_fields = {"slug": ("title",)}
