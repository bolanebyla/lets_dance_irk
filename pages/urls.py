from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('lessons/<str:direction>', views.allDirectionLessons),
    path('lessons/<str:direction>/<str:lesson_name>', views.oneLesson),

    path('news/item/1', views.item_news),

    path('articles/item/<str:slug>', views.item_articles),
    path('articles/<str:slug>', views.category_articles),

    path('news', views.news),
    path('articles', views.articles),

    path('', views.index, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
