from django import forms
from django.contrib import admin
from .models import Articles, ArticlesCategories, LessonsBallroomDancing, LessonsPreschoolers, LessonsSchoolStudents

from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Методические материалы
class ArticlesCategoriesForm(forms.ModelForm):
    class Meta:
        model = ArticlesCategories
        fields = '__all__'


class ArticlesCategoriesAdmin(admin.ModelAdmin):
    form = ArticlesCategoriesForm
    prepopulated_fields = {'slug': ('category',)}


admin.site.register(ArticlesCategories, ArticlesCategoriesAdmin)


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


# Бальные танцы
class LessonsBallroomDancingAdminForm(forms.ModelForm):
    text = forms.CharField(label='Основной текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = LessonsBallroomDancing
        fields = '__all__'


class LessonsBallroomDancingAdmin(admin.ModelAdmin):
    form = LessonsBallroomDancingAdminForm


# admin.site.register(LessonsBallroomDancing, LessonsBallroomDancingAdmin)


# =======================================================================#

# Дошкольники
class LessonsPreschoolersAdminForm(forms.ModelForm):
    text = forms.CharField(label='Основной текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = LessonsPreschoolers
        fields = '__all__'


class LessonsPreschoolersAdmin(admin.ModelAdmin):
    form = LessonsPreschoolersAdminForm


# admin.site.register(LessonsPreschoolers, LessonsPreschoolersAdmin)


# =======================================================================#

# Школьники
class LessonsSchoolStudentsAdminForm(forms.ModelForm):
    text = forms.CharField(label='Основной текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = LessonsSchoolStudents
        fields = '__all__'


class LessonsSchoolStudentsAdmin(admin.ModelAdmin):
    form = LessonsSchoolStudentsAdminForm

# admin.site.register(LessonsSchoolStudents, LessonsSchoolStudentsAdmin)

# =======================================================================#
