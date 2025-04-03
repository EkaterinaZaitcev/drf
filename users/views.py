from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer

from users.models import CustomsUser, Payment
from users.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ('payment_course','payment_lesson','method',)
    ordering_fields = ('payment_date',)


class CustomsUserViewSet(viewsets.ModelViewSet):
    queryset = CustomsUser.objects.all()
    serializer_class = UserSerializer
