from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from .models import Cart, CartProduct
from rest_framework import mixins, viewsets
from .serializers import (
    CartSerializer,
    CartProductSerializer,
)
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class CartViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    serializer_class = CartSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class CartProductViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = CartProductSerializer
    lookup_field = "id"

    def get_queryset(self):
        return CartProduct.objects.filter(cart__user=self.request.user)