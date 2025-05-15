from rest_framework import serializers
from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['name', 'email', 'address', 'phone', 'items', 'total']
        read_only_fields = ['order_id', 'created_at', 'updated_at']

class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order   
        fields = ['status']

       