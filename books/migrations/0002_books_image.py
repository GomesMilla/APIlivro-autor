# Generated by Django 3.2 on 2021-04-13 11:38

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=books.models.upload_image_book),
        ),
    ]
