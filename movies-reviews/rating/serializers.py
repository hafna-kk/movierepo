from .models import Movie
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    rating = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'name', 'slug', 'image', 'price',
                  'qty', 'inventory', 'description', 'rating']
