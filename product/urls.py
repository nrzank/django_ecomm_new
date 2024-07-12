from django.urls import path
from product import views


urlpatterns = [

    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),

    path('categories/<int:category_id>/products/', views.ProductByCategoryListView.as_view(), name='product-by-category'),
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),

    path('cart/', views.CartListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', views.CartDetailView.as_view(), name='cart-detail'),

    path('cart/items/', views.CartItemListCreateView.as_view(), name='cartitem-list-create'),
    path('cart/items/<int:pk>/', views.CartItemDetailView.as_view(), name='cartitem-detail'),
    path('cart/clear/', views.CartClearView.as_view(), name='cart-clear'),

    path('orders/', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),

    path('jsonplaceholder/', views.APIPosts.as_view()),









]
