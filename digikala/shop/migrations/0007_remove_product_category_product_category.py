# Generated by Django 5.0.7 on 2024-08-14 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_product_category_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Category',
        ),
        migrations.AddField(
            model_name='product',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
    ]