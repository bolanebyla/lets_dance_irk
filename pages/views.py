from django.shortcuts import render, HttpResponse
from .models import LessonsSchoolStudents, LessonsPreschoolers, LessonsBallroomDancing


def index(request):
    return render(request, 'pages/index.html', {'main_active': 'active'})


# =======================================================================#


# Бальные танцы
def LessonsBallroomDancing_list(request):
    lessons = LessonsBallroomDancing.objects.all()

    data = []
    for lesson in lessons:
        data.append(
            {
                'name': lesson.name,
                'description': lesson.description,
            }
        )
    page_name = 'Бальные танцы'
    name = 'BallroomDancing'

    return render(request, 'pages/lessons_list.html',
                  {'lessons_active': 'active', 'name': name, 'page_name': page_name, 'lessons': data})


def lessonBallroomDancing(request):
    lessons = LessonsBallroomDancing.objects.all()
    all_lessons = []
    for lesson in lessons:
        all_lessons.append(
            {
                'name': lesson.name,
                'lessons_active': 'active'
            }
        )

    name = request.GET.get("name", 0)
    lesson = LessonsBallroomDancing.objects.get(name=name)
    data = {
        'direction': 'BallroomDancing',
        'direction_name': 'Бальные танцы',
        'name': lesson.name,
        'text': lesson.text,
        'lessons': all_lessons,
        'link': 'LessonsBallroomDancing',
        'lessons_active': 'active',

    }
    return render(request, 'pages/lesson.html', data)


# =======================================================================#


# Для дошкольников

def LessonsPreschoolers_list(request):
    lessons = LessonsPreschoolers.objects.all()

    data = []
    for lesson in lessons:
        data.append(
            {
                'name': lesson.name,
                'description': lesson.description,
            }
        )
    page_name = 'Дошкольники'
    name = 'Preschoolers'

    return render(request, 'pages/lessons_list.html',
                  {'lessons_active': 'active', 'name': name, 'page_name': page_name, 'lessons': data})


def lessonPreschoolers(request):
    lessons = LessonsPreschoolers.objects.all()
    all_lessons = []
    for lesson in lessons:
        all_lessons.append(
            {
                'name': lesson.name,
                'lessons_active': 'active',
            }
        )

    name = request.GET.get("name", 0)
    lesson = LessonsPreschoolers.objects.get(name=name)
    data = {
        'direction': 'Preschoolers',
        'direction_name': 'Дошкольники',
        'name': lesson.name,
        'text': lesson.text,
        'lessons': all_lessons,
        'link': 'LessonsPreschoolers',
        'lessons_active': 'active',

    }
    return render(request, 'pages/lesson.html', data)


# =======================================================================#


# Для школьников

def LessonsSchoolStudents_list(request):
    lessons = LessonsSchoolStudents.objects.all()

    data = []
    for lesson in lessons:
        data.append(
            {
                'name': lesson.name,
                'description': lesson.description,
            }
        )
    page_name = 'Школьники'
    name = 'SchoolStudents'

    return render(request, 'pages/lessons_list.html',
                  {'lessons_active': 'active', 'name': name, 'page_name': page_name, 'lessons': data})


def lessonSchoolStudents(request):
    lessons = LessonsSchoolStudents.objects.all()
    all_lessons = []
    for lesson in lessons:
        all_lessons.append(
            {
                'name': lesson.name,
                'lessons_active': 'active',
            }
        )

    name = request.GET.get("name", 0)
    lesson = LessonsSchoolStudents.objects.get(name=name)
    data = {
        'direction': 'Preschoolers',
        'direction_name': 'Школьники',
        'name': lesson.name,
        'text': lesson.text,
        'lessons': all_lessons,
        'link': 'LessonsSchoolStudents'

    }
    return render(request, 'pages/lesson.html', data)
