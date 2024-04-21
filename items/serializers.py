from rest_framework import serializers
from .models import Product
from reviews.serializers import ReviewSerializer


class ProductSerializer(serializers.ModelSerializer):
    #productReview = ReviewSerializer(many=True, read_only=True)
    #amountOfReviews = serializers.Field()

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "body",
            "price",
            "amount",
            "amountOfReviews",
            "average",
        ]
