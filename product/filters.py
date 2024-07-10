from django_filters import rest_framework as filters

from product.models import Product


class ProductFilterSet(filters.DjangoFilterBackend):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = {
            'name': ['exact', 'contains', 'icontains'],

        }

