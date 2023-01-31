from django.urls import path, include
from .views import *
from .serializers import MenuItemSerializer
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'menuitem', MenuItemViewSet)

urlpatterns = [
    path('', main_page, name='main'),
    path('dishes/', ShowAllDishes.as_view(), name='all_dishes'),
    path('filter/', FilterMenuItemView.as_view(), name='filter'),
    path('search/', Search.as_view(), name='search'),

    path('food/', ShowAllKitchen.as_view(), name='kitchen'),
    path('bar/', ShowAllBar.as_view(), name='show_all_bar'),
    path('create-dish/', CreateDish.as_view(), name='add_dish'),
    path('create-subcategory/', CreateSubCategory.as_view(), name='add_subcategory'),
    
    
    path('api/v1/', include(router.urls)),
]