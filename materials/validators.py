from rest_framework import serializers

class URLValidator:
    def __call__(self, value):
        """Валидатор на проверку сторонних ссылок кроме YouTube"""

        # Проверяем, что ссылка начинается с http:// или https://
        if value not in ['http://youtube.com', 'https://youtube.com']:
            raise serializers.ValidationError('URL не может содержать внешних ресурсов')
        return value
