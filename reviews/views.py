from django.shortcuts import render
from .serializers import ReviewSerializer
from .models import Review
from rest_framework import mixins, viewsets
# Create your views here.

class ReviewViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    serializer_class = ReviewSerializer
    lookup_field = "id"

    def get_queryset(self):
        # review_id = self.kwargs.get("id")
        # if review_id:
        #     return Review.objects.filter(id=review_id)
        # else:
        product_name = self.request.query_params.get("productname")
        if product_name:
            return Review.objects.filter(product__title=product_name)
        return Review.objects.all()
