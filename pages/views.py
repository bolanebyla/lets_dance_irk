from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Articles, ArticlesCategories, LessonsSchoolStudents, LessonsPreschoolers, LessonsBallroomDancing


def index(request):
    return render(request, 'pages/index.html', {'main_active': 'active'})


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
    data = {
        'posts': posts,
        'categories': categories,
        'page': page
    }
    return render(request, 'pages/articles.html', data)


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


def item_articles(request, slug):
    post = Articles.objects.filter(slug=slug)
    categories = ArticlesCategories.objects.all()
    data = {
        'post': post[0],
        'categories': categories
    }
    return render(request, 'pages/item_articles.html', data)


def news(request):
    data = {}
    return render(request, 'pages/news.html', data)


def item_news(request):
    data = {}
    return render(request, 'pages/item_news.html', data)


# =======================================================================#

# Список всех уроков направления
def allDirectionLessons(request, direction):
    tables = {'Бальные танцы': LessonsBallroomDancing, 'Дошкольники': LessonsPreschoolers,
              'Школьники': LessonsSchoolStudents}
    try:
        table = tables[direction]
    except KeyError:
        return HttpResponseNotFound()

    lessons = table.objects.all()
    lessons_data = []
    for lesson in lessons:
        lessons_data.append(
            {
                'name': lesson.name,
                'description': lesson.description,
            }
        )
    data = {
        'lessons': lessons_data,
        'lessons_active': 'active',
        'direction': direction
    }
    return render(request, 'pages/lessons_list.html', data)


# Один урок направления
def oneLesson(request, direction, lesson_name):
    tables = {'Бальные танцы': LessonsBallroomDancing, 'Дошкольники': LessonsPreschoolers,
              'Школьники': LessonsSchoolStudents}
    try:
        table = tables[direction]
    except KeyError:
        return HttpResponseNotFound()

    lessons = table.objects.all()
    all_lessons = []
    for lesson in lessons:
        all_lessons.append(
            {
                'name': lesson.name,
                'lessons_active': 'active'
            }
        )

    try:
        lesson = table.objects.get(name=lesson_name)
    except:
        return HttpResponseNotFound()

    data = {
        'direction': direction,
        'name': lesson.name,
        'text': lesson.text,
        'lessons': all_lessons,
        'lessons_active': 'active',

    }

    return render(request, 'pages/lesson.html', data)
