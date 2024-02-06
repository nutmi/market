from django.shortcuts import render
from .models import Product
from rest_framework import mixins, viewsets
from .serializers import ProductSerializer


# Create your views here.
class ProductViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = ProductSerializer
    lookup_field = "id"
    ordering_fields = ["price", "amount"]
    ordering_param = "sort"

    def get_queryset(self):
        ordering = self.request.query_params.get(self.ordering_param)
        if ordering in self.ordering_fields:
            return Product.objects.all().order_by(f"-{ordering}")
        return Product.objects.all()
