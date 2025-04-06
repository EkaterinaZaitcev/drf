from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(email="test1@mail.ru", first_name="admin1", last_name="admin1")
        user.set_password("1234567890")
        user.save()
