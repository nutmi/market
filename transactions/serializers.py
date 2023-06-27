from rest_framework import serializers
from .models import Vallet


class ValletSerializer(serializers.ModelSerializer):
    amount = serializers.IntegerField(write_only=True)

    class Meta:
        model = Vallet
        fields = ["user", "balance", "amount"]
        read_only_fields = ["user", "balance"]

    def create(self, validated_data):
        validated_data.pop("amount", None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        number = validated_data.get("amount")

        instance.balance += number
        instance.save()
        return instance  # instance = model:vallet
