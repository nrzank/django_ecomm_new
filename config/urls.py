from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('product.urls')),
    path('categories/', include('product.urls')),
    path('auth/', include('authorization.urls')),
    path('cart/', include('cart.urls')),
]
