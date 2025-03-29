from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView
from tutorial.quickstart.serializers import UserSerializer

from users.models import User, Payment
from users.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ('payment_course','payment_lesson','method',)
    ordering_fields = ('payment_date',)


class CustomsUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
