# Generated by Django 3.0.4 on 2020-03-29 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonsBallroomDancing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название урока')),
                ('description', models.TextField(verbose_name='Краткое описание урока')),
                ('text', models.TextField(verbose_name='Основной текст')),
            ],
        ),
        migrations.CreateModel(
            name='LessonsPreschoolers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название урока')),
                ('description', models.TextField(verbose_name='Краткое описание урока')),
                ('text', models.TextField(verbose_name='Основной текст')),
            ],
        ),
        migrations.CreateModel(
            name='LessonsSchoolStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название урока')),
                ('description', models.TextField(verbose_name='Краткое описание урока')),
                ('text', models.TextField(verbose_name='Основной текст')),
            ],
        ),
        migrations.DeleteModel(
            name='Videos',
        ),
    ]
