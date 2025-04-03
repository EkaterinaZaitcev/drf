from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from tutorial.quickstart.serializers import UserSerializer

from users.models import CustomsUser, Payment
from users.serializers import PaymentSerializer, CustomsUserSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ('payment_course','payment_lesson','method',)
    ordering_fields = ('payment_date',)


class CustomsUserViewSet(viewsets.ModelViewSet):
    queryset = CustomsUser.objects.all()
    serializer_class = UserSerializer


class CustomsUserCreateAPIView(CreateAPIView):
    serializer_class = CustomsUserSerializer
    queryset = CustomsUser.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
