from rest_framework import serializers
from .models import Review
from .models import Review
from core.models import OrderItem
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["user", "text", "score", "product", "views"]
        read_only_fields = ["views"]
    
    def create(self, validated_data):
        product = validated_data.get("product")
        user = validated_data.get("user")
        print(product.title)
        product(user.username)