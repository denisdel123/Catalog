# Generated by Django 5.0.2 on 2024-02-21 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='catalogApp', verbose_name='Изображение')),
                ('price_for_pcs', models.IntegerField(verbose_name='Стоимость за штуку')),
                ('create_date', models.DateField(verbose_name='Дата создания')),
                ('last_change_date', models.DateField(verbose_name='Дата последнего изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogApp.category', verbose_name='Категория')),
            ],
        ),
    ]
