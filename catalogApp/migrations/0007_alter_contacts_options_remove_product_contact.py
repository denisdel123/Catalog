# Generated by Django 5.0.2 on 2024-02-26 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogApp', '0006_product_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='contact',
        ),
    ]
