# Generated by Django 5.0.7 on 2024-08-14 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Category',
        ),
        migrations.AddField(
            model_name='product',
            name='Category',
            field=models.ManyToManyField(to='shop.category'),
        ),
    ]