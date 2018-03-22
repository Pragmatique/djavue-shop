from rest_framework import routers

from .views import ProductViewSet,OrderViewSet,ProductInOrderViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'order', OrderViewSet)
router.register(r'productsinorder', ProductInOrderViewSet)
urlpatterns = router.urls
