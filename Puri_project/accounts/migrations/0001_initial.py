# Generated by Django 4.1.4 on 2023-01-19 19:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restoraunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название ресторана')),
                ('adress', models.CharField(max_length=200, verbose_name='Адрес ресторана')),
                ('employee', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]