from rest_framework.serializers import ModelSerializer

from users.models import Payment, CustomsUser


class PaymentSerializer(ModelSerializer):
    """Сериализатор для платежей"""

    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(ModelSerializer):
    """Сериализатор для пользователя"""

    payments = PaymentSerializer(many=True)

    class Meta:
        model = CustomsUser
        fields = "__all__"


class CustomsUserSerializer(ModelSerializer):
    class Meta:
        model = CustomsUser
        fields = "__all__"


class CustomsUserDetailSerializer(ModelSerializer):
    payment_history = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = CustomsUser
        fields = ["id", "email", "phone_number", "avatar", "city", "payment_history"]
