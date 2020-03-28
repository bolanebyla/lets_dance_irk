from django.urls import path
from . import views


urlpatterns = [
    path('video_lessons_test', views.video_test, name='video_test'),
    path('', views.index, name='home'),

    ]