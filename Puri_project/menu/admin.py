from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'subcategory', 'create_date', 'update_date', ]
    filter_horizontal = ['compound', 'sauce']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category' ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Compound)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]