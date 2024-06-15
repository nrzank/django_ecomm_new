from django.contrib.auth import get_user_model
from django.db import models



class Category(models.Model):
    name = models.CharField(255, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def __str__(self):
        return f'{self.pk} {self.name}'





class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def __str__(self):
        return f'{self.pk} {self.name}'




#
# class Order(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#     status = models.CharField(max_length=20, default='processing')
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     @property
#     def __str__(self):
#         return f'{self.pk} {self.user}'
#
#
#
# class OrderItem(models.Model):
#     order = models.ForeignKey('Order', on_delete=models.CASCADE)
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#
#
#
# class Review(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     rating = models.IntegerField()
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"Review by {self.user} for {self.product.name}"
#
#
#
# class Cart(models.Model):
#     user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"Cart of {self.user}"
#
#
#
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"{self.quantity} of {self.product.name} in cart of {self.cart}"
