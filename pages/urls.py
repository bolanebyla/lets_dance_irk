from django.urls import path

from . import views

urlpatterns = [
    path('news/item/1', views.item_news),

    path('articles/item/<str:slug>', views.item_articles),
    path('articles/<str:slug>', views.category_articles),

    path('news', views.news),
    path('articles', views.articles),
    path('successful_entry', views.successful_entry),
    path('', views.index, name='home'),
]



