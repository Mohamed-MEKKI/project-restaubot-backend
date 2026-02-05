from django.http import BadHeaderError, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail, BadHeaderError


from restaurants.models import restaurants
from restaurants.serializers import RestaurantSerializer, ContactMessagesSerializer

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
    return redirect('get all restaurants')


@api_view(['POST'])
def send_email(request):
    message = request.data.get("message", "")
    from_email = request.data.get("email", "")
    if message and from_email:
        try:
            send_mail(
                subject="Test message",
                message=message,
                from_email=from_email,
                recipient_list=[from_email],
                fail_silently=False
            )
        except BadHeaderError:
            return Response({"error": "Invalid header found."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Email sent successfully."}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Make sure all fields are entered and valid."}, status=status.HTTP_400_BAD_REQUEST)