import json
from rest_framework import generics, filters, status, views, permissions
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import requests
from django_filters.rest_framework import DjangoFilterBackend

from .exeptions import PermissionDeniedException
from .filters import ProductFilterSet
from .models import Category, Product, Cart, CartItem, Order, OrderItem
from .serializers import (CategorySerializer,
                          ProductSerializer,
                          CartSerializer,
                          CartItemSerializer,
                          OrderSerializer
                          )


# Category views
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Product views
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilterSet
    filter_backends = [DjangoFilterBackend, SearchFilter]
    ordering_fields = ['price', 'created_at', 'updated_at']
    search_fields = ['name', 'description']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.get_object().user != self.request.user:
            raise PermissionDeniedException()
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDeniedException()
        instance.delete()


# Cart views
class CartListCreateView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        cart = serializer.save(user=self.request.user)
        self.update_cart_total_price(cart)

    def perform_update(self, serializer):
        cart = serializer.save()
        self.update_cart_total_price(cart)

    def update_cart_total_price(self, cart):
        total_price = sum(item.product.price * item.quantity for item in cart.items.all())
        cart.total_price = total_price
        cart.save()


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        cart = serializer.save()
        self.update_cart_total_price(cart)

    def update_cart_total_price(self, cart):
        total_price = sum(item.product.price * item.quantity for item in cart.items.all())
        cart.total_price = total_price
        cart.save()


# CartItem views
class CartItemListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)
        self.update_cart_total_price(cart)

    def perform_update(self, serializer):
        cart_item = serializer.save()
        self.update_cart_total_price(cart_item.cart)

    def perform_destroy(self, instance):
        cart = instance.cart
        instance.delete()
        self.update_cart_total_price(cart)

    def update_cart_total_price(self, cart):
        total_price = sum(item.product.price * item.quantity for item in cart.items.all())
        cart.total_price = total_price
        cart.save()


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def perform_update(self, serializer):
        cart_item = serializer.save()
        self.update_cart_total_price(cart_item.cart)

    def perform_destroy(self, instance):
        cart = instance.cart
        instance.delete()
        self.update_cart_total_price(cart)

    def update_cart_total_price(self, cart):
        total_price = sum(item.product.price * item.quantity for item in cart.items.all())
        cart.total_price = total_price
        cart.save()


# Order views
class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        cart = Cart.objects.get(user=self.request.user)
        cart_items = cart.items.all()

        total_price = sum(item.product.price * item.quantity for item in cart_items)

        order = serializer.save(user=self.request.user, cart=cart, status='created', total_price=total_price)

        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity,
                                     price=item.product.price)

        cart.items.all().delete()
        cart.total_price = 0
        cart.save()


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


# Category products views
class ProductByCategoryListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = ProductFilterSet
    ordering_fields = ['price', 'created_at', 'updated_at']
    search_fields = ['name', 'description']

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)


# Cart Clear View
class CartClearView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart.items.all().delete()
        cart.total_price = 0
        cart.save()
        return Response({"detail": "Cart has been cleared"}, status=status.HTTP_200_OK)


class APIPosts(views.APIView):

    def get(self, request, *args, **kwargs):
        posts = requests.get('https://jsonplaceholder.typicode.com/posts/')
        return Response(json.loads(posts.content))


