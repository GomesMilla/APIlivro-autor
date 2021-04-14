# Generated by Django 3.2 on 2021-04-13 20:39

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210413_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=books.models.upload_image_book),
        ),
        migrations.AlterField(
            model_name='author',
            name='city',
            field=models.CharField(max_length=90, verbose_name='Cidade de nascimento:'),
        ),
    ]
