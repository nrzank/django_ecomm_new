from django.urls import path
from product.views import (CategoryListCreateView, CategoryRetrieveUpdateDestroyView,
                           ProductListCreateView, ProductRetrieveUpdateDestroyView,
                           CartListCreateView, CartDetailView, CartItemListCreateView, CartItemDetailView,
                           OrderListCreateView, OrderDetailView, ReviewListCreateView, ReviewDetailView,
                           WishlistListCreateView, WishlistDetailView, ProductByCategoryListView)







urlpatterns = [

    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),

    path('categories/<int:category_id>/products/', ProductByCategoryListView.as_view(), name='product-by-category'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),

    path('cart/', CartListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),

    path('cart/items/', CartItemListCreateView.as_view(), name='cartitem-list-create'),
    path('cart/items/<int:pk>/', CartItemDetailView.as_view(), name='cartitem-detail'),

    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),

    path('wishlists/', WishlistListCreateView.as_view(), name='wishlist-list-create'),
    path('wishlists/<int:pk>/', WishlistDetailView.as_view(), name='wishlist-detail'),
]
