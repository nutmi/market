from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart, CartProduct, Order, OrderItem
from django.shortcuts import get_object_or_404
from items.models import Product
from rest_framework import mixins, viewsets
from .serializers import CartProductSerializer, OrderItemSeraializer, OrderSeraializer
from transactions.models import Vallet
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated
import random
from django.contrib.auth.models import User

# Create your views here.


class CartViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CartProductSerializer
    lookup_field = "id"

    def get_queryset(self):
        cart_products = CartProduct.objects.filter(cart__user=self.request.user)
        return cart_products

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        cart_product_prices = [item.full_price for item in queryset]
        total_price = sum(cart_product_prices)
        serializer = self.get_serializer(queryset, many=True)
        data = {
            "cart_products": serializer.data,
            "total_price": total_price,
        }
        return Response(data)


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
