from django.urls import path, include
from .views import *


urlpatterns = [
    path('register/', RegisterUserPage, name='register' ),
    path('login/', loginPage, name='login' ),
    path('logout/', logoutUser, name='logout' ),

]
