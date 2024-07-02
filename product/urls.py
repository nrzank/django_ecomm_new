from django.urls import path
from .views import (CategoryListCreateView,
                    CategoryRetrieveUpdateDestroyView,
                    ProductListCreateView,
                    ProductRetrieveUpdateDestroyView,
                    CartListCreateView,
                    CartDetailView,
                    CartItemListCreateView,
                    CartItemDetailView,
                    OrderListCreateView,
                    OrderDetailView,
                    OrderItemListCreateView,
                    OrderItemDetailView)

urlpatterns = [
    # Category
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),

    # Product
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),

    # Cart
    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),

    # CartItem
    path('cart-items/', CartItemListCreateView.as_view(), name='cartitem-list-create'),
    path('cart-items/<int:pk>/', CartItemDetailView.as_view(), name='cartitem-detail'),

    # Order URLs
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

    # OrderItem URLs
    path('order-items/', OrderItemListCreateView.as_view(), name='orderitem-list-create'),
    path('order-items/<int:pk>/', OrderItemDetailView.as_view(), name='orderitem-detail'),
]
