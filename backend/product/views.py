from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductDetailview(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def perform_create(self,serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if not content :
            content=title
        serializer.save(content=content)
        
    


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

