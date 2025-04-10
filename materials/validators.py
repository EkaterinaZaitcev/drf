from rest_framework import serializers
from urllib.parse import urlparse

def URLValidator(value):
        """Валидатор на проверку сторонних ссылок кроме YouTube"""

        if "youtube.com" not in value:
            raise serializers.ValidationError('URL не может содержать внешних ресурсов')
        return value
