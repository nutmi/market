from django.contrib import admin
from .models import Cart, CartProduct, Order, OrderItem

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(OrderItem)
admin.site.register(Order)
