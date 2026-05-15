from rest_framework import serializers
from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'user', 'name', 'email', 'address', 'menu_item', 'phone', 'status', 'total']
        read_only_fields = ['user', 'created_at', 'updated_at']

class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order   
        fields = ['status']

       