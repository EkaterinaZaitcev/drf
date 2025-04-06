from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import CustomUserCreateAPIView, PaymentsViewSet, CustomUserListAPIView, \
    CustomUserRetrieveAPIView, CustomUserDestroyAPIView, CustomUserUpdateAPIView

router = SimpleRouter()


router.register(r"payments", PaymentsViewSet, basename="payments")
#router.register(r"users", CustomUserListAPIView, basename="users")

app_name = UsersConfig.name

urlpatterns = [
    path("register/", CustomUserCreateAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
    path("users",CustomUserListAPIView.as_view(), name="user_list"),
    path("users/<int:pk>/", CustomUserRetrieveAPIView.as_view(), name="user_detail"),
    path("users/<int:pk>/delete", CustomUserDestroyAPIView.as_view(), name="user_delete"),
    path("users/<int:pk>/update", CustomUserUpdateAPIView.as_view(), name="user_update"),
]

urlpatterns += router.urls
