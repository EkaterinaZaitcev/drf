from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("У пользователя должна быть почта")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Суперпользователь должен иметь is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Суперпользователь должен иметь is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


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

    objects = UserManager() # Подключаем кастомный менеджер

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
         return self.email


class Payment(models.Model):
    """Класс платежи"""
    PAYMENT_METHOD_CHOICES = [
        ("card", "Карта"),
        ("cash", "Наличные"),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="payments", verbose_name="Пользователь")
    payment_date = models.DateField(auto_now_add=True, verbose_name="Дата оплаты")
    payment_course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE,
                                    verbose_name="Оплаченный курс")
    payment_lesson = models.ForeignKey(Lesson, null=True, blank=True, on_delete=models.CASCADE,
                                    verbose_name="Оплаченный урок")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма оплаты")
    method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES, verbose_name="способ оплаты")

    def __str__(self):
        return f"{self.owner} - {self.amount} - {self.payment_date}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ["-payment_date"]
