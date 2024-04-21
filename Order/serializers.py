from rest_framework import serializers
from .models import OrderItem, Order

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

        if not user.cart.items.count():
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
            return order