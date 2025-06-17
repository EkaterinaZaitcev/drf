from rest_framework import serializers


def url_validator(value):
    """Валидатор на проверку сторонних ссылок кроме YouTube"""

    if "youtube.com" not in value:
        raise serializers.ValidationError("URL не может содержать внешних ресурсов")
    return value
