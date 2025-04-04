from rest_framework import serializers
from restaurants.models import restaurants

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = restaurants
        fields = '__all__'