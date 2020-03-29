from django import forms
from django.contrib import admin
from .models import LessonsBallroomDancing, LessonsPreschoolers, LessonsSchoolStudents

from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Бальные танцы
class LessonsBallroomDancingAdminForm(forms.ModelForm):
    text = forms.CharField(label='Основной текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = LessonsBallroomDancing
        fields = '__all__'


class LessonsBallroomDancingAdmin(admin.ModelAdmin):
    form = LessonsBallroomDancingAdminForm


admin.site.register(LessonsBallroomDancing, LessonsBallroomDancingAdmin)


# =======================================================================#

# Дошкольники
class LessonsPreschoolersAdminForm(forms.ModelForm):
    text = forms.CharField(label='Основной текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = LessonsPreschoolers
        fields = '__all__'


class LessonsPreschoolersAdmin(admin.ModelAdmin):
    form = LessonsPreschoolersAdminForm


admin.site.register(LessonsPreschoolers, LessonsPreschoolersAdmin)


# =======================================================================#

# Школьники
class LessonsSchoolStudentsAdminForm(forms.ModelForm):
    text = forms.CharField(label='Основной текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = LessonsSchoolStudents
        fields = '__all__'


class LessonsSchoolStudentsAdmin(admin.ModelAdmin):
    form = LessonsSchoolStudentsAdminForm


admin.site.register(LessonsSchoolStudents, LessonsSchoolStudentsAdmin)

# =======================================================================#
