# Generated by Django 3.2 on 2021-04-13 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210413_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='lives',
            field=models.CharField(default=1, max_length=60, verbose_name='Cidade onde vive:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='about',
            field=models.TextField(max_length=5000, verbose_name='Sobre o autor:'),
        ),
    ]
