from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import CustomUser, Payments


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class CustomUserDetailSerializer(serializers.ModelSerializer):
    payment_history = PaymentsSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "email", "phone_number", "avatar", "city", "payment_history"]


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "password",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "city",
            "avatar",
            )

class UserBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "email",
            "phone_number",
            "city",
            "avatar",
        )