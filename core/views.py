from rest_framework.response import Response
from .models import Cart, Order, OrderItem, CartProduct
from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from .serializers import (
    CartSerializer,
    CartProductSerializer,
    OrderItemSeraializer,
    OrderSeraializer,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class CartViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    authentication_classes = [TokenAuthentication]
    serializer_class = CartSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class CartProductViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    authentication_classes = [TokenAuthentication]
    serializer_class = CartProductSerializer
    lookup_field = "id"

    def get_queryset(self):
        return CartProduct.objects.filter(cart__user=self.request.user)


class OrderViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSeraializer
    lookup_field = "id"

    def get_queryset(self):
        orders = Order.objects.filter(user=self.request.user)
        return orders

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderItemViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderItemSeraializer
    lookup_field = "id"

    def get_queryset(self):
        order_items = OrderItem.objects.filter(order__user=self.request.user)
        return order_items

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        order_product_prices = [item.full_price for item in queryset]
        total_price = sum(order_product_prices)
        serializer = self.get_serializer(queryset, many=True)
        data = {
            "cart_products": serializer.data,
            "total_price": total_price,
            "cart_product_prices": order_product_prices,
        }
        return Response(data)
