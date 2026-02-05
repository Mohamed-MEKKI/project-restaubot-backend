from rest_framework import serializers
from restaurants.models import restaurants, ContactMessages

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = restaurants
        fields = '__all__'

class ContactMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessages
        fields = '__all__'