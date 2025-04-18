from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from materials.models import Course, Subscribe
from users.models import CustomUser


@shared_task
def send_mail_course_update(course_id):
    """Рассылка сообщений об обновлении курса"""
    course = get_object_or_404(Course, id=course_id)
    subscription_course = Subscribe.objects.all()
    for sub in subscription_course:
        print(f"Отправка электронного письма на {Subscribe.user.email}")
        send_mail(
            from_email=EMAIL_HOST_USER,
            recipient_list=[Subscribe.user.email],
            message = f'Здравствуйте! Сообщаем, что в курсе "{course.name}" обновления!',
            fail_silently=False
        )


@shared_task
def last_login():
    """Проверка последнее входа"""
    users = CustomUser.objects.filter(last_login=False)
    today = timezone.now()
    for user in users:
        if today - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()
            print(f"Пользователь {user.email} отключен")
        else:
            print(f"Пользователь {user.email} активен")
