# Generated by Django 3.0.4 on 2020-06-01 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_articles_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlescategories',
            name='categories',
            field=models.CharField(max_length=30),
        ),
    ]
