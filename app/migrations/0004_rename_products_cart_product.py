# Generated by Django 5.0.3 on 2024-03-17 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='products',
            new_name='product',
        ),
    ]
