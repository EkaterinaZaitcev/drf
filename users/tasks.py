from datetime import timedelta, timezone

from celery import shared_task

from dateutil.utils import today

from users.models import CustomUser


@shared_task
def last_login():
    """Проверка последнее входа"""
    now = timezone.now()
    month_ago = now - timedelta(days=30)
    users = CustomUser.objects.filter(last_login__lt=month_ago, is_active=True)
    for user in users:
        if user.count() > 0:
            user.update(is_active=False)
            user.save()
        else:
            print(f"Пользователь {user.email} активен")
