# Generated by Django 3.2.13 on 2022-06-01 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_total_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='total_rate',
        ),
    ]
