from datetime import *
from django.utils import timezone

from django.core.management.base import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        course1 = Course.objects.get(id=1)
        lesson1 = Lesson.objects.get(id=2)

        sample_data = [
            {
                "id": 1,
                "payment_date": timezone.now(),
                "payment_course": course1,
                "payment_lesson": None,
                "amount": 100.00,
                "method": "наличные",
            },
            {
                "id": 2,
                "payment_date": timezone.now(),
                "payment_course": None,
                "payment_lesson": lesson1,
                "amount": 50.00,
                "method": "перевод на счет",
            }
        ]

        for item in sample_data:
            Payment.objects.create(**item)
        self.stdout.write(self.style.SUCCESS("Данные успешно загружены!"))
