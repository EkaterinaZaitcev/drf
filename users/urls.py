from rest_framework.routers import SimpleRouter
from users.apps import UsersConfig


from users.views import PaymentViewSet, UserViewSet

router = SimpleRouter()


router.register(r'payments', PaymentViewSet, basename='payments')
router.register(r'users', UserViewSet, basename='users')
app_name = UsersConfig.name

urlpatterns = []

urlpatterns += router.urls