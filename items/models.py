from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self) -> str:
        return self.title

    @property
    def amountOfReviews(self):
        total = 0
        for _ in self.productReview.all():
            total += 1
        return total

    @property
    def average(self):
        total = 0
        for i in self.productReview.all():
            total += i.score
        return total / self.amountOfReviews
