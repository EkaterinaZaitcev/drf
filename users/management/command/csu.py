from django.core.management import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = CustomUser.objects.create(email="admin@mail.ru")
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password("1234567890")
        user.save()
