# Generated by Django 4.1.2 on 2022-10-22 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0006_remove_product_photos_product_photos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='photos',
        ),
        migrations.AddField(
            model_name='product',
            name='photoLoad',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
