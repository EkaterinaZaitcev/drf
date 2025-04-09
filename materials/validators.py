from rest_framework import serializers
from urllib.parse import urlparse

class URLValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        """Валидатор на проверку сторонних ссылок кроме YouTube"""

        url = 'https://www.youtube.com/watch?v=nn7l5e94CwI&ab_channel=PythonChannel'
        value = urlparse(url)

        # Проверяем, что ссылка начинается с http:// или https://
        if value.netloc not in ['http://youtube.com', 'https://youtube.com']:
            raise serializers.ValidationError('URL не может содержать внешних ресурсов')
        return value
