from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MenuItem, SubCategory, Category



class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'
        labels = {
            'name': 'Название',
            'compound': 'Состав',
            'weight': 'Выход блюда',
            'description': 'Красочное описание',
            'sauce': 'Состав соуса/заправки',
            'subcategory': 'Подкатегория',
        }


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'
        labels = {
            'name': 'Название',
            'category': 'категория',
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'username', 'password1', 'password2' ]
