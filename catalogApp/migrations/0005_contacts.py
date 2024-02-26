# Generated by Django 5.0.2 on 2024-02-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogApp', '0004_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
            ],
            options={
                'verbose_name': 'Контакты',
            },
        ),
    ]
