from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
# Register your models here.


@admin.register(Restoraunt)
class RestorauntAdmin(admin.ModelAdmin):
    list_display = ['title', 'adress']
    list_editable = ['adress']
    filter_horizontal = ['employee']

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'first_name', 'last_name']