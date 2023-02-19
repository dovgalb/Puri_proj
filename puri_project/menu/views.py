from django.shortcuts import render
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from accounts.decorators import *

from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.db.models import Q
from rest_framework import generics, viewsets
from .serializers import MenuItemSerializer
from accounts.views import UserAccesMixin


def main_page(request):
    return render(request, 'menu/index.html')


class SubCategoryBarEat(View):
    # Возвращает все подкатегории напитков в сайд баре
    def get_subcat_bar(self, *args, **kwargs):
        return SubCategory.objects.filter(category_id='2')

    """возвращает все подкатегории кухни в сайдбаре"""

    def get_subcat_eat(self, *args, **kwargs):
        return SubCategory.objects.filter(category_id='1')


class ShowAllDishes(UserAccesMixin, SubCategoryBarEat, ListView):
    """Возвращает все блюда"""
    raise_exception = False
    permission_required = 'menu.view_menuitem'

    template_name = 'menu/all_dishes.html'
    model = MenuItem
    context_object_name = 'menu_items'


class ShowAllKitchen(UserAccesMixin, SubCategoryBarEat, ListView):
    """Возвращает все блюда кухни"""
    permission_required = 'menu.view_menuitem'

    template_name = 'menu/all_dishes.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        return MenuItem.objects.filter(category=2)


class ShowAllBar(UserAccesMixin, SubCategoryBarEat, ListView):
    """Возвращает весь бар"""
    permission_required = 'menu.view_menuitem'

    template_name = 'menu/all_dishes.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        return MenuItem.objects.filter(category=4)


class Search(UserAccesMixin, SubCategoryBarEat, ListView):
    """Поиск по названию блюда, составу, составу соуса или заправки"""
    permission_required = 'menu.view_menuitem'

    def get_queryset(self):
        queryset = MenuItem.objects.filter(
            Q(name__iregex=self.request.GET.get('search')) |
            Q(compound__name__iregex=self.request.GET.get('search')) |
            Q(compound__compound__name__iregex=self.request.GET.get('search')) |
            Q(sauce__name__iregex=self.request.GET.get('search'))
        ).distinct()
        return queryset


# def search_test(request):
#     if request.method == "POST":
#         searched = request.POST['searched']
#         search_dishes = MenuItem.objects.filter(name__contains=searched)
#         return render(request, 'menu/search.html', context={'searched': searched,
#                                                             'search_dishes': search_dishes })
#     else:
#         return render(request, 'menu/search.html', context={})


class FilterMenuItemView(UserAccesMixin, SubCategoryBarEat, ListView):
    """чекбокс фильтр менюайтемов по категориям"""
    permission_required = ('menu.view_menuitem')

    def get_queryset(self):
        queryset = MenuItem.objects.filter(
            Q(subcategory_id__in=self.request.GET.getlist('bar_category')) |
            Q(subcategory_id__in=self.request.GET.getlist('eat_category'))
        )
        return queryset

    ######################################################################################


class CreateDish(CreateView):
    """Создает блюдо"""
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'menu/create_dish.html'
    success_url = '/dishes'


class CreateSubCategory(CreateView):
    """Создает подкатегорию"""
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'menu/create_subcategory.html'
    success_url = '/dishes'


######################################################################################
"""API"""


class MenuItemViewSet(viewsets.ModelViewSet):
    """ModelViewSet для menuitem"""
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
