from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

    @property
    def full_price(self):
        return sum(item.full_price for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    title = models.CharField(max_length=100)
    body = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveSmallIntegerField(default=1)

    @property
    def full_price(self):
        return self.price * self.quantity