# Generated by Django 3.0.4 on 2020-06-06 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0028_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='url',
            field=models.CharField(max_length=250, unique=True, verbose_name='Ссылка на альбом из Вк'),
        ),
    ]