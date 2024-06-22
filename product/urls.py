from django.contrib import admin
from django.urls import path, include
from product import views


urlpatterns = [
    path('', views.ProductListAPIview.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailAPIview.as_view(), name='product_list')
    ]
