# Generated by Django 3.0.4 on 2020-03-28 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
