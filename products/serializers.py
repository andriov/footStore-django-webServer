from rest_framework import serializers
from .models import Product


# Serializers allow complex data such as querysets (the result
# of queries) and model instances to be converted to native
# Python datatypes, which can then be converted into JSON or XML.
# It also provides conversion of the other way around (deseriali-
# zation), allowing parsed data to be converted back into complex
# Python objects, after validating the data.


# This serializer is for the model Product.

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id_user','name', 'description', 'stock','cost','image')
