from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson
from users.models import Payment, User


class PaymentSerializer(ModelSerializer):
    """Сериализатор для платежей"""

    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(ModelSerializer):
    """Сериализатор для пользователя"""

    payments = PaymentSerializer(many=True)

    class Meta:
        model = User
        fields = "__all__"
    class Meta:
        model = Course
        fields = '__all__'
