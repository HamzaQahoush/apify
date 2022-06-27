from django.db import router
from rest_framework.routers import DefaultRouter

from product.viewsets import ProductViewSet


router=DefaultRouter()
"""
creating the routers:
http://127.0.0.1:8000/api/v2/products_rv2/
"""
router.register('products_rv2',ProductViewSet, basename='products')


urlpatterns=router.urls