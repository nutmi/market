from django.db import models
from django.contrib.auth import get_user_model
from items.models import Product

# Create your models here.

User = get_user_model()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="productReview"
    )
    text = models.CharField(max_length=150)
    score = models.IntegerField(default=0)
