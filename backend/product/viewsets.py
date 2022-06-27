from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

"""
 to combine the logic for a set of related views in a single class
"""
class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field= 'pk'