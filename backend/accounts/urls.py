from rest_framework import routers

from .views import LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView

router = routers.DefaultRouter()
router.register(r'user', UserRetrieveUpdateAPIView.as_view(), base_name="UserUpdate")
router.register(r'users', RegistrationAPIView.as_view(), base_name="User")
router.register(r'users/login', LoginAPIView.as_view(), base_name="Login")
urlpatterns = router.urls