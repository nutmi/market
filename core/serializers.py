from rest_framework import serializers
from .models import CartProduct, Cart, OrderItem, Order
from transactions.models import Vallet
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


class OrderItemSeraializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["order", "title", "body", "quantity", "id", "price"]


class OrderSeraializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["user"]
        read_only_fields = fields

    def create(self, validated_data):
        user = validated_data["user"]
        vallet = Vallet.objects.get(user=user)
        cart_total = user.cart.full_price
        if not user.cart.items.count() == 0:
            if cart_total <= vallet.balance:
                order = Order.objects.create(user=user)
                for cart_item in user.cart.items.all():
                    OrderItem.objects.create(
                        order=order,
                        title=cart_item.product.title,
                        body=cart_item.product.body,
                        price=cart_item.product.price,
                        quantity=cart_item.quantity,
                    )
                user.cart.items.all().delete()
                vallet.balance -= cart_total
                vallet.save()
                return order
            else:
                raise serializers.ValidationError(
                    {"message": "not enough money in your wallet"}
                )
        else:
            raise serializers.ValidationError(
                {"message": "there is nothing in you cart"}
            )
