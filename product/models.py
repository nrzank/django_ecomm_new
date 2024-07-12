from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} {self.name}'


class Product(models.Model):
    IN_STOCK, LOW_STOCK, OUT_OF_STOCK = 'in_stock', 'low_stock', 'out_of_stock'
    STOCK = (
        (IN_STOCK, 'В наличии'),
        (LOW_STOCK, 'Мало на складе'),
        (OUT_OF_STOCK, 'Нет в наличии'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.CharField(max_length=20, choices=STOCK, default=IN_STOCK)
    image = models.ImageField(upload_to='images/', null=True, blank=True, default=None)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name='products', on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} {self.name}'


class Cart(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Cart({self.user})'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'CartItem({self.product}, {self.quantity})'


class Order(models.Model):
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('processed', 'Processed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order({self.pk}, {self.user}, {self.status})'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'OrderItem({self.product}, {self.quantity})'


