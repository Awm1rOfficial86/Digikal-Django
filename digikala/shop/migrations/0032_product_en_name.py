# Generated by Django 5.0.7 on 2024-08-19 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0031_product_bime'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='En_Name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]