from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from restaurants.models import restaurants
from restaurants.serializers import RestaurantSerializer

@api_view(['GET'])
def get_all_responses(request):
    serialized_data = RestaurantSerializer(restaurants.objects.all(), many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_one_response(request, restaurant_id):
    restaurant = get_object_or_404(restaurants, id=restaurant_id)
    serialized_data = RestaurantSerializer(restaurant)
    return Response(serialized_data.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_restaurant_item(request):
    serialized_data = RestaurantSerializer(data=request.data)

    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)

    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(restaurants, id=restaurant_id)
    serialized_data = RestaurantSerializer(restaurant, data=request.data)

    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(restaurants, id=restaurant_id)
    restaurant.delete()
    return Response({"message": "Menu item deleted successfully"}, status=status.HTTP_200_OK)
