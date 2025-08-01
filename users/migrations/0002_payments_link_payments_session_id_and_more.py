# Generated by Django 5.1.7 on 2025-04-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payments",
            name="link",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="Ссылка на оплату"
            ),
        ),
        migrations.AddField(
            model_name="payments",
            name="session_id",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="ID сессии"
            ),
        ),
        migrations.AlterField(
            model_name="payments",
            name="payment_method",
            field=models.CharField(
                choices=[
                    ("наличные", "наличные"),
                    ("перевод на счет", "перевод на счет"),
                ],
                max_length=50,
                verbose_name="Способ оплаты",
            ),
        ),
    ]
