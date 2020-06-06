# -----------------------------------------------------------------------------------#
#
# pages/models.py
# ===================
# 1. Категории методических матриалов
# 2. Методические материалы
# 3. Новости
# 4. Галерея
#
# -----------------------------------------------------------------------------------#

from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User


# ----------------------------------------#
# 1. Категории методических матриалов
# ----------------------------------------#
class ArticlesCategories(models.Model):
    category = models.CharField('Категория', max_length=250, unique=True)
    slug = models.SlugField('Ссылка', max_length=250, unique=True)

    class Meta:
        verbose_name = 'категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category


# ----------------------------------------#
# 2. Методические материалы
# ----------------------------------------#
class Articles(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    )
    title = models.CharField('Название', max_length=250)
    category = models.ForeignKey(ArticlesCategories, on_delete=models.DO_NOTHING)
    slug = models.SlugField('Ссылка', max_length=250, unique=True)
    cover = models.ImageField('Превью', upload_to='images/')
    author = models.CharField('Автор', max_length=250)
    description = models.TextField('Описание')
    body = models.TextField('Основной текст')
    # publish = models.DateField('Дата публикации', default=date.today)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата последнего редактирования', auto_now=True)
    status = models.CharField('Статус', max_length=15, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-updated',)
        verbose_name = 'методические материалы'
        verbose_name_plural = 'Методические материалы'

    def __str__(self):
        return self.title


# ----------------------------------------#
# 3. Новости
# ----------------------------------------#
class News(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    )
    title = models.CharField('Название', max_length=250)
    slug = models.SlugField('Ссылка', max_length=250, unique=True)
    cover = models.ImageField('Превью', upload_to='images/')
    description = models.TextField('Описание')
    body = models.TextField('Основной текст')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата последнего редактирования', auto_now=True)
    status = models.CharField('Статус', max_length=15, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


# ----------------------------------------#
# 4. Галерея
# ----------------------------------------#
class Gallery(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Скрыто'),
        ('published', 'Опубликовано'),
    )
    title = models.CharField('Название', max_length=250)
    url = models.CharField('Ссылка на альбом из Вк', unique=True, max_length=250)
    cover = models.ImageField('Обложка', upload_to='images/gallery')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    status = models.CharField('Статус', max_length=15, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'альбом галереи'
        verbose_name_plural = 'Альбомы галереии'

    def __str__(self):
        return self.title
