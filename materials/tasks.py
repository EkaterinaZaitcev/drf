from celery import shared_task
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from config.settings import EMAIL_HOST_USER
from materials.models import Course, Subscribe


@shared_task
def send_mail_course_update(course_id):
    """Рассылка сообщений об обновлении курса"""
    course = get_object_or_404(Course, id=course_id)
    subscription_course = Subscribe.objects.filter(course)
    for sub in subscription_course:
        send_mail(
            from_email=EMAIL_HOST_USER,
            recipient_list=[sub.user.email],
            message = f'Здравствуйте! Сообщаем, что в курсе "{course.name}" обновления!',
            fail_silently=False
        )
