# Generated by Django 5.0.4 on 2024-06-11 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
