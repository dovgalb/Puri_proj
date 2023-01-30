from django.db import models
from pytils.translit import slugify
from django.urls import reverse

# Create your models here.


class MenuItem(models.Model):
    name = models.CharField(max_length=200, verbose_name='Блюдо')
    compound = models.TextField(blank=True, verbose_name='Состав')
    weight = models.PositiveIntegerField(blank=True, verbose_name='Выход блюда (граммов)', null=True)
    sauce = models.TextField(blank=True, verbose_name='Соус/Заправка', null=True)
    description = models.TextField(blank=True, verbose_name='Красочное описание', null=True)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True, verbose_name='Подкатегория')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    create_date = models.DateField(verbose_name='Дата создания', auto_now_add=True, null=True )
    update_date = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True, null=True)
    image = models.FileField(verbose_name='Фото блюда', upload_to='menu_images/', blank=True)

    def __str__(self):
        return f'{self.name}|{self.subcategory}'


class SubCategory(models.Model):
    name = models.CharField(max_length=30, verbose_name='Подкатегория')
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL, verbose_name='Категория')
    slug = models.SlugField(default='', null=False, db_index=True, blank=True, unique=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('show_subcategory_item', args=[self.slug])


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name