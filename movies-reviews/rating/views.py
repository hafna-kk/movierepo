from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import ProductSerializer
from .models import Movie


# Get all products in random order

class ProductViewSet(viewsets.ModelViewSet):
    # Ensure that the related Rating instances are included
    queryset = Movie.objects.all().order_by('?').prefetch_related('rating')
    serializer_class = ProductSerializer
