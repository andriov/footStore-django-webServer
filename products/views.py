from django.shortcuts import render
from django.http import HttpResponse
from .serializers import ProductSerializer
from rest_framework import generics
from .models import Product
# Views take a Web request and returns a Web response.


# Index view for testing purposes only
def index(request):
    return HttpResponse("Prueba index.")


# This view list all available products inside the database
# for testing purposes.

class ProductList(generics.ListCreateAPIView):
    queryset = Product.name
    serializer_class = ProductSerializer


