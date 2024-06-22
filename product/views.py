from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import views, request, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


from product.models import Product
from product.serializers import ProductSerializer


# Create your views here.



class ProductListAPIview(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIview(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class ProductListAPIview(views.APIView):
#
#     def get(self, response, *args, **kwargs):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#
#         return Response(serializer.data)
#
#
