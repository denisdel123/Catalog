from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Наименование'
        verbose_name_plural = 'Наименования'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='catalogImage/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price_for_pcs = models.IntegerField(verbose_name='Стоимость за штуку')
    create_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    last_change_date = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Наименование'
        verbose_name_plural = 'Наименования'
