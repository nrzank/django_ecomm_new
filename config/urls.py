from django.contrib import admin
from django.urls import path, include




# project_name/urls.py



urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('product.urls')),
    path('auth/', include('authorization.urls'))
]
