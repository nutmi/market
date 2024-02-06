from django.db import models
from django.contrib.auth.models import User
from items.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

    @property
    def full_price(self):
        total = 0
        for item in self.items.all():
            total += item.full_price
        return total


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    @property
    def full_price(self):
        return self.product.price * self.quantity

    def delete_items(self):
        self.delete()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

    @property
    def full_price(self):
        total = 0
        all_items = self.items.all()
        for item in all_items:
            a = item.full_price
            total += a
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveSmallIntegerField(default=1)

    @property
    def full_price(self):
        return self.price * self.quantity
