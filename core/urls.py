from django.contrib import admin
from django.urls import path
from .views import CartViewSet, CartProductViewSet, OrderViewSet, OrderItemViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"cart", CartViewSet, basename="carts")
router.register(r"cartproducts", CartProductViewSet, basename="cartproducts")
router.register(r"order", OrderItemViewSet, basename="order")
router.register(r"orders", OrderViewSet, basename="orders")
urlpatterns = router.urls

urlpatterns += []
