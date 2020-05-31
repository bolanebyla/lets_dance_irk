from django.urls import path
from . import views

urlpatterns = [
    path('lessons/<str:direction>', views.allDirectionLessons),
    path('lessons/<str:direction>/<str:lesson_name>', views.oneLesson),
    path('news', views.news),
    path('articles', views.articles),


    path('', views.index, name='home'),

]
