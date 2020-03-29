from django.urls import path
from . import views

urlpatterns = [
    # path('video_lessons_test', views.video_test, name='video_test'),
    path('LessonsBallroomDancing', views.LessonsBallroomDancing_list),
    path('lessons/BallroomDancing', views.lessonBallroomDancing),

    path('LessonsPreschoolers', views.LessonsPreschoolers_list),
    path('lessons/Preschoolers', views.lessonPreschoolers),

    path('LessonsSchoolStudents', views.LessonsSchoolStudents_list),
    path('lessons/SchoolStudents', views.lessonSchoolStudents),

    path('', views.index, name='home'),

]
