# Generated by Django 5.0.7 on 2024-08-20 06:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0048_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
    ]