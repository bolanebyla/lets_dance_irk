# Generated by Django 3.0.4 on 2020-06-01 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20200601_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='description',
            field=models.CharField(default='Пустое поле', max_length=1000, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
