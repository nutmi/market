from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self) -> str:
        return self.title
