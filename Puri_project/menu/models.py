from django.db import models
from pytils.translit import slugify
from django.urls import reverse


# Create your models here.


class MenuItem(models.Model):
    name = models.CharField(max_length=200, verbose_name='Блюдо')
    compound = models.ManyToManyField('Compound', blank=True, related_name='related_compound',
                                      verbose_name='Состав блюда')
    weight = models.PositiveIntegerField(blank=True, verbose_name='Выход блюда (граммов)', null=True)
    sauce = models.ManyToManyField('Compound', blank=True, related_name='related_sauce', verbose_name='Состав соуса')
    description = models.TextField(blank=True, verbose_name='Красочное описание', null=True)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True, verbose_name='Подкатегория')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    create_date = models.DateField(verbose_name='Дата создания', auto_now_add=True, null=True)
    update_date = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True, null=True)
    image = models.FileField(verbose_name='Фото блюда', upload_to='menu_images/', blank=True)

    def __str__(self):
        return f'{self.name}|{self.subcategory}'

    class Meta:
        verbose_name = "Блюдо или напиток"
        verbose_name_plural = "Блюда и напитки"


class Compound(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название ингридиента')
    compound = models.ManyToManyField('Compound', blank=True, related_name='related_compound_compound',
                                      verbose_name='Состав ингридиента')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ингридиент"
        verbose_name_plural = "Ингридиенты"


class SubCategory(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название подкатегории')
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL, verbose_name='Категория')
    slug = models.SlugField(default='', null=False, db_index=True, blank=True, unique=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('show_subcategory_item', args=[self.slug])

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
