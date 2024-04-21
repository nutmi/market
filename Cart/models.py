from django.db import models
from django.contrib.auth import get_user_model
from items.models import Product
# Create your models here.
User = get_user_model()

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

    @property
    def full_price(self):
        return sum(item.full_price for item in self.items.all())


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    @property
    def full_price(self):
        return self.product.price * self.quantity

    def delete_items(self):
        self.delete()