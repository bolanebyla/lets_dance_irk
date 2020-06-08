# -----------------------------------------------------------------------------------#
#
# pages/views.py
# ===================
# 1. Главная
# 2. Успешная запись на занятие
# 3. Категории методических матриалов
# 4. Методические материалы
# 5. Одна статья
# 6. Новости
# 7. Одна новость
# 8. Галерея
# 9. Фотографии одного альбома галереи + Парсер фото из Вк
#
# -----------------------------------------------------------------------------------#

import requests
import json

from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Articles, ArticlesCategories, News, Gallery
from .forms import ModalLesson
from lets_dance_irk.email_config import EMAIL_TO_SEND

from . import vk_config


# ----------------------------------------#
# 1. Главная
# ----------------------------------------#
def index(request):
    if request.method == 'POST':
        # Form was submitted
        form = ModalLesson(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            child_name = cd['child_name']
            age = cd['age']
            parent_name = cd['parent_name']
            phone_number = cd['phone_number']
            subject = f'Пробное занятие {age}'
            message = f'ФИО ребёнка: {child_name}\n' \
                      f'Возраст: {age}\n' \
                      f'ФИО родителя: {parent_name}\n' \
                      f'Номер телефона: {phone_number}'
            send_mail(subject, message, 'admin@myblog.com', [EMAIL_TO_SEND], fail_silently=False)
            return HttpResponseRedirect('successful_entry')

    else:
        form = ModalLesson()
    last_news = News.objects.filter(status='published')[:2]  # Последние две новости
    albums = Gallery.objects.filter(status='published')[:3]  # Последние три альбома
    data = {
        'form': form,
        'news': last_news,
        'albums': albums
    }
    return render(request, 'pages/index.html', data)


# ----------------------------------------#
# 2. Успешная запись на занятие
# ----------------------------------------#
def successful_entry(request):
    return render(request, 'pages/successful_entry.html')


# ----------------------------------------#
# 3. Категории методических матриалов
# ----------------------------------------#
def category_articles(request, slug):
    category = ArticlesCategories.objects.filter(slug=slug)
    posts = Articles.objects.filter(status='published').filter(category=category[0].id)
    categories = ArticlesCategories.objects.all()
    data = {
        'category': category[0].category,
        'posts': posts,
        'categories': categories
    }
    return render(request, 'pages/articles.html', data)


# ----------------------------------------#
# 4. Методические материалы
# ----------------------------------------#
def articles(request):
    object_list = Articles.objects.filter(status='published')
    paginator = Paginator(object_list, 10)  # 10 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    categories = ArticlesCategories.objects.all()
    last_news = News.objects.filter(status='published')[:10]
    data = {
        'posts': posts,
        'categories': categories,
        'page': page,
        'last_news': last_news
    }
    return render(request, 'pages/articles.html', data)


# ----------------------------------------#
# 5. Одна статья
# ----------------------------------------#
def item_articles(request, slug):
    post = Articles.objects.filter(slug=slug)
    categories = ArticlesCategories.objects.all()
    last_news = News.objects.filter(status='published')[:10]
    last_articles = Articles.objects.filter(status='published')[:10]
    data = {
        'post': post[0],
        'categories': categories,
        'last_news': last_news,
        'last_posts': last_articles
    }
    return render(request, 'pages/item_articles.html', data)


# ----------------------------------------#
# 6. Новости
# ----------------------------------------#
def news(request):
    object_list = News.objects.filter(status='published')
    paginator = Paginator(object_list, 10)  # 10 posts in each page
    page = request.GET.get('page')
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        news_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        news_list = paginator.page(paginator.num_pages)

    last_articles = Articles.objects.filter(status='published')[:10]
    data = {
        'news': news_list,
        'page': page,
        'last_posts': last_articles
    }
    return render(request, 'pages/news.html', data)


# ----------------------------------------#
# 7. Одна новость
# ----------------------------------------#
def item_news(request, slug):
    news_item = News.objects.filter(slug=slug)[0]
    album = news_item.album
    photo = None
    if album:
        url = album.url
        photo = get_photo_from_vk(url)[:8]


    last_articles = Articles.objects.filter(status='published')[:10]
    last_news = News.objects.filter(status='published')[:10]
    data = {
        'news': news_item,
        'album': album,
        'photo': photo,
        'last_posts': last_articles,
        'last_news': last_news
    }
    return render(request, 'pages/item_news.html', data)


# ----------------------------------------#
# 8. Галерея
# ----------------------------------------#

def gallery(request):
    object_list = Gallery.objects.filter(status='published')
    paginator = Paginator(object_list, 30)  # 30 albums in each page
    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        albums = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        albums = paginator.page(paginator.num_pages)

    last_articles = Articles.objects.filter(status='published')[:10]
    last_news = News.objects.filter(status='published')[:10]

    data = {
        'albums': albums,
        'page': page,
        'last_posts': last_articles,
        'last_news': last_news
    }
    return render(request, 'pages/gallery.html', data)


# ----------------------------------------#
# 9. Фотографии одного альбома галереи
# ----------------------------------------#
def get_photo_from_vk(url):  # Парсер фотографий из альбома Вк
    url = url.split('_')
    owner_id = '-' + ''.join(x for x in url[0] if x.isdigit())
    album_id = url[1]
    access_token = vk_config.ACCESS_TOKEN
    version = vk_config.VERSION
    response = requests.get(
        f'https://api.vk.com/method/photos.get?owner_id={owner_id}&album_id={album_id}&access_token={access_token}&v={version}')
    items = json.loads(response.content)['response']['items']
    photo = []
    for item in items:
        small_img = item['sizes'][2]
        big_img = item['sizes'][-1]
        photo.append(
            {
                'small_img': small_img,
                'big_img': big_img
            }
        )
    return photo


def album_photos(request, id):
    album = Gallery.objects.filter(id=id)[0]
    url = album.url
    photo = get_photo_from_vk(url)
    last_articles = Articles.objects.filter(status='published')[:10]
    last_news = News.objects.filter(status='published')[:10]
    data = {
        'photo': photo,
        'last_posts': last_articles,
        'last_news': last_news,
        'album': album

    }
    return render(request, 'pages/album_photos.html', data)
