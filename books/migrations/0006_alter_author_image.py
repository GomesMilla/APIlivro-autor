# Generated by Django 3.2 on 2021-04-13 20:43

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20210413_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=books.models.upload_image_author),
        ),
    ]
