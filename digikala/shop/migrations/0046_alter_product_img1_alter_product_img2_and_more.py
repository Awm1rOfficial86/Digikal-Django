# Generated by Django 5.0.7 on 2024-08-19 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0045_product_img1_product_img2_product_img3_product_img4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Img1',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='upload/products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Img2',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='upload/products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Img3',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='upload/products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Img4',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='upload/products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Img5',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='upload/products/'),
        ),
    ]
