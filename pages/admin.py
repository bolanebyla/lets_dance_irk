# -----------------------------------------------------------------------------------#
#
# pages/admin.py
# ===================
# 1. Категории методических матриалов
# 2. Методические материалы
# 3. Новости
#
# -----------------------------------------------------------------------------------#

from django import forms
from django.contrib import admin
from .models import Articles, ArticlesCategories, News, Gallery

from ckeditor_uploader.widgets import CKEditorUploadingWidget


# ----------------------------------------#
# 1. Категории методических матриалов
# ----------------------------------------#
class ArticlesCategoriesForm(forms.ModelForm):
    class Meta:
        model = ArticlesCategories
        fields = '__all__'


class ArticlesCategoriesAdmin(admin.ModelAdmin):
    form = ArticlesCategoriesForm
    prepopulated_fields = {'slug': ('category',)}


admin.site.register(ArticlesCategories, ArticlesCategoriesAdmin)


# ----------------------------------------#
# 2. Методические материалы
# ----------------------------------------#
class ArticlesAdminForm(forms.ModelForm):
    body = forms.CharField(label='Основной текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = Articles
        fields = '__all__'


class ArticlesAdmin(admin.ModelAdmin):
    form = ArticlesAdminForm
    list_display = ('title', 'slug', 'category', 'author', 'updated', 'status')
    list_filter = ('status', 'updated', 'created', 'category', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'updated'
    ordering = ('status', 'updated')


admin.site.register(Articles, ArticlesAdmin)


# ----------------------------------------#
# 3. Новости
# ----------------------------------------#
class NewsAdminForm(forms.ModelForm):
    body = forms.CharField(label='Основной текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = ArticlesAdminForm
    list_display = ('title', 'slug', 'created', 'updated', 'status')
    list_filter = ('status', 'updated', 'created')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'updated'
    ordering = ('status', 'updated')


admin.site.register(News, NewsAdmin)


# ----------------------------------------#
# 4. Галерея
# ----------------------------------------#

admin.site.register(Gallery)