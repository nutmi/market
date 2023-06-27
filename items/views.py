from django.shortcuts import render
from .models import Product
from rest_framework import generics, mixins, status, viewsets
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer


# Create your views here.
class GenericAPIView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "id"
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
