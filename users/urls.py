from django.urls import include, path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    CustomUserCreateAPIView,
    CustomUserDestroyAPIView,
    CustomUserListAPIView,
    CustomUserRetrieveAPIView,
    CustomUserUpdateAPIView,
    PaymentsCreateAPIView,
)

app_name = UsersConfig.name

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("register/", CustomUserCreateAPIView.as_view(), name="register"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("users", CustomUserListAPIView.as_view(), name="user_list"),
    path("users/<int:pk>/", CustomUserRetrieveAPIView.as_view(), name="user_detail"),
    path(
        "users/<int:pk>/delete", CustomUserDestroyAPIView.as_view(), name="user_delete"
    ),
    path(
        "users/<int:pk>/update", CustomUserUpdateAPIView.as_view(), name="user_update"
    ),
    path(
        "pay/course/<int:course_id>/",
        PaymentsCreateAPIView.as_view(),
        name="pay_course",
    ),
]

urlpatterns += router.urls
