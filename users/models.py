from tkinter.constants import CASCADE

from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Укажите телефон",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        verbose_name="Загрузите аватар",
    )
    country = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    """Класс платежи"""
    PAYMENT_METHOD_CHOICES = [
        ("card", "Карта"),
        ("cash", "Наличные"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="payments", verbose_name="Пользователь")
    payment_date = models.DateField(auto_now_add=True, verbose_name="Дата оплаты")
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE,
                                    verbose_name="Оплаченный курс")
    lesson = models.ForeignKey(Lesson, null=True, blank=True, on_delete=models.CASCADE,
                                    verbose_name="Оплаченный урок")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма оплаты")
    method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES, verbose_name="способ оплаты")

    def __str__(self):
        return f"{self.user} - {self.amount} - {self.payment_date}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ["-payment_date"]
