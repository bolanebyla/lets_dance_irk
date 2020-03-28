from django.shortcuts import render, HttpResponse
from .models import Videos


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def video_test(request):
    videos = Videos.objects.all()
    print(videos)

    data = []
    for video in videos:
        url = video.url.split('=')[-1]
        data.append(
            {
                'url': url,
                'name': video.name,
                'description': video.description
            }
        )
    return render(request, 'pages/video_lessons.html', {'lesson_name': 'Видео уроки для дошкольников', 'videos': data})
