# Generated by Django 3.0.4 on 2020-06-06 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_auto_20200606_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='cover',
            field=models.ImageField(upload_to='images/gallery', verbose_name='Обложка'),
        ),
    ]
