# Generated by Django 3.0.4 on 2020-06-01 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_auto_20200601_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlescategories',
            name='updated',
        ),
        migrations.AlterField(
            model_name='articlescategories',
            name='slug',
            field=models.SlugField(max_length=250, verbose_name='Ссылка'),
        ),
    ]
