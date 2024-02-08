from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Cart, Order
from transactions.models import Vallet

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_related_models(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
        Vallet.objects.create(user=instance)
