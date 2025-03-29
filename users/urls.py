from rest_framework.routers import SimpleRouter
from users.apps import UsersConfig


from users.views import PaymentViewSet, CustomsUserViewSet

router = SimpleRouter()


router.register(r'payments', PaymentViewSet, basename='payments')
router.register(r'users', CustomsUserViewSet, basename='users')
app_name = UsersConfig.name

urlpatterns = []

urlpatterns += router.urls