from rest_framework import serializers
from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id','name', 'email', 'address','menu_item' ,'phone', 'total']
        read_only_fields = ['created_at', 'updated_at']

class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order   
        fields = ['status']

       