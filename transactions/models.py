from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Vallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=100, decimal_places=2, default=0)
