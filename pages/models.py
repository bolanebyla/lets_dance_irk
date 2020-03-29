from django.db import models


class LessonsPreschoolers(models.Model):
    name = models.CharField('Название урока', max_length=150)
    description = models.TextField('Краткое описание урока')
    text = models.TextField('Основной текст')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок для дошкольников'
        verbose_name_plural = 'Уроки для дошкольников'


class LessonsSchoolStudents(models.Model):
    name = models.CharField('Название урока', max_length=150)
    description = models.TextField('Краткое описание урока')
    text = models.TextField('Основной текст')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок для школьников'
        verbose_name_plural = 'Уроки для школьников'


class LessonsBallroomDancing(models.Model):
    name = models.CharField('Название урока', max_length=150)
    description = models.TextField('Краткое описание урока')
    text = models.TextField('Основной текст')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок по бальным танцам'
        verbose_name_plural = 'Уроки по бальным танцам'
