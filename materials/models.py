from django.db import models
from django.conf import settings


class Course(models.Model):
    """Класс курс"""

    name = models.CharField(
        max_length=255, verbose_name="Название курса", help_text="Укажите курс"
    )
    preview = models.ImageField(
        upload_to="materials/preview", verbose_name="Превью", blank=True, null=True
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание курса",
        help_text="Укажите описание курса",
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Слушатель",
                              help_text="Укажите слушателя", )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """Класс урок"""

    name = models.CharField(
        max_length=255, verbose_name="Название урока", help_text="Укажите урок"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Курс", help_text="Выберите курс", blank=True, null=True
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание урока",
        help_text="Укажите описание урока",
    )
    preview = models.ImageField(
        upload_to="materials/preview", verbose_name="Превью", blank=True, null=True
    )
    video_link = models.URLField(
        blank=True,
        null=True,
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео урока",
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Слушатель",
                              help_text="Укажите слушателя", )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
