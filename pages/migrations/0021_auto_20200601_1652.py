# Generated by Django 3.0.4 on 2020-06-01 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_auto_20200601_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlescategories',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default='', verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articlescategories',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='created', verbose_name='Ссылка'),
        ),
    ]
