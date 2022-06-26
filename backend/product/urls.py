from django.urls import URLPattern, path

from . import views

# generic view to show the product details by id

# api/products/
urlpatterns = [
    path("<int:pk>/", views.ProductDetailview.as_view()),
    path("", views.ProductListCreateAPIView.as_view()),
    path("<int:pk>/update/", views.ProductUpdateView.as_view()),
    path("<int:pk>/delete/", views.ProductDeleteView.as_view()),
]
