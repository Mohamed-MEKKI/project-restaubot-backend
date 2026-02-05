from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from order.models import Order
from order.serializers import OrderSerializer, UpdateOrderSerializer

import datetime
from django.utils import timezone


@api_view(['GET'])
def get_all_responses(request):
    serialized_data = OrderSerializer(Order.objects.all(), many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_one_order(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    serialized_data = UpdateOrderSerializer(order, data=request.data)

    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_one_response(request, phone_number):
    now = timezone.now()
    fifteens_minutes_from_creation = now - datetime.timedelta(minutes = 15)
    
    orders = Order.objects.filter(
        phone = phone_number,
        created_at__gte=fifteens_minutes_from_creation,
        created_at__lte=now
    )
    
    if (orders.exists()):
        serialized_data = OrderSerializer(orders, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    return Response(serialized_data.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_order(request):
    serialized_data = OrderSerializer(data=request.data)

    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)

    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_order(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    serialized_data = OrderSerializer(order, data=request.data)

    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_order_status(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    serialized_data = UpdateOrderSerializer(order, data=request.data)

    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_order(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    order.delete()
    return redirect('get all orders')

@api_view(['DELETE'])
def delete_order_in_chatbot(request, phone_number):
    now = timezone.now()
    fifteens_minutes_from_creation = now - datetime.timedelta(minutes = 15)
    
    order = Order.objects.filter(
        phone = phone_number,
        created_at__gte=fifteens_minutes_from_creation,
        created_at__lte=now
    ).first()
    if order:
        order.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_all_orders(request):
    orders = Order.objects.all()
    orders.delete()
    return redirect('get all orders')  # Redirect to the list of orders after deletion