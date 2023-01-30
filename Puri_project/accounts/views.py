from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import PermissionRequiredMixin

from .decorators import *
from .forms import *
from .models import *


# Create your views here.
class UserAccesMixin(PermissionRequiredMixin):
    """Если пользователь не авторизован, то перенаправляет его на страницу авторизации, 
    если авторизован но нет доступа, то перенаправляет на главную страницу"""
    def dispatch(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(),
                                     self.get_login_url(),
                                     self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('main')
        return super(UserAccesMixin, self).dispatch(request, *args, **kwargs)


@unauthenticated_user
def RegisterUserPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            """показывает флеш сообщения после успешного редиректа"""
            messages.success(request, f'Аккаунт "{user}" - успешно создан.' )
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)        


@unauthenticated_user
def loginPage(request):
    """Авторизация пользователя"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Не правильное имя пользователя или пароль')

    context={}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

        
    
    
