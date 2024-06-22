from rest_framework import serializers
from product.models import Product, Category


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'stock', 'category')




class CategorySerializer(serializers.Serializer):

    class Meta:
        model = Category
        fields = ('name', 'description')
