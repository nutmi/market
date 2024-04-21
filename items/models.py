from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    amount = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.title

    @property
    def amountOfReviews(self):
        return self.productReview.count()

    @property
    def average(self):
        total = sum(i.score for i in self.productReview.all())
        if total != 0:
            return total / self.amountOfReviews
        return 0
