from django.contrib import admin
from django.urls import path
from .views import CartViewSet, OrderViewSet, OrderItemViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"cart", CartViewSet, basename="carts")
router.register(r"order", OrderItemViewSet, basename="order")
router.register(r"orders", OrderViewSet, basename="orders")
urlpatterns = router.urls

urlpatterns += []
