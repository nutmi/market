from rest_framework import serializers
from .models import CartProduct, Cart
from items.models import Product

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ["cart", "product", "quantity", "id", "full_price"]

    def create(self, validated_data):
        product = Product.objects.get(id=validated_data.get("product").id)
        quantity = validated_data.get("quantity")
        if quantity > product.amount:
            raise serializers.ValidationError("no more")
        product.amount -= quantity
        product.save()
        return CartProduct.objects.create(**validated_data)


class CartSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    items = CartProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "username", "items", "full_price"]