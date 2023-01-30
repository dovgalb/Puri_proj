from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Restoraunt(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название ресторана')
    city = models.CharField(max_length=50, default='Нет Данных', verbose_name='Город')
    adress = models.CharField(max_length=200, verbose_name='Адрес ресторана')
    employee = models.ManyToManyField(User)



