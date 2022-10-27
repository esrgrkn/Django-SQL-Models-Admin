# Generated by Django 4.1.2 on 2022-10-22 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0002_alter_product_imageurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='imageUrl',
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', verbose_name='photo/%Y/%m/%d'),
        ),
    ]