from django.contrib.auth import get_user_model
from django.db import models


from product.models import Product


class Cart(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.pk}"

    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.total_price()
        return total


class CartItem(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def total_price(self):
        return self.quantity * self.product.price
