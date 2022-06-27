from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator

"""
This method to validate attrribute in api
"""
def validate_title( value):
    # check if exact match , iexcat -> case sensative
    qs = Product.objects.filter(title__exact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product name")
    return value

 