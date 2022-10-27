# Generated by Django 4.1.2 on 2022-10-22 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0004_remove_product_photo_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='photo_t',
        ),
        migrations.AddField(
            model_name='product',
            name='photos',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='ProjectApp.photo'),
        ),
    ]
