from django.urls import path
from .views import CartViewSet, CartProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"cart", CartViewSet, basename="carts")
router.register(r"cartproducts", CartProductViewSet, basename="cartproducts")
urlpatterns = router.urls

urlpatterns += []