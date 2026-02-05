from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from user.models import User
from user.serializers import UserSerializers


@api_view(['GET'])
def get_all_users(request):
    serialized_data = UserSerializers(User.objects.all(), many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    serialized_data = UserSerializers(user)
    return Response(serialized_data.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_user(request):
    serialized_data = UserSerializers(data=request.data)

    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)

    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    serialized_data = UserSerializers(user, data=request.data)

    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_user(user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('get users')


@api_view(['DELETE'])
def delete_all_users():
    users =User.objects.all()
    if not users:
        return Response({"message": "No users to delete"}, status=status.HTTP_404_NOT_FOUND)
    users.delete()
    return redirect('get users')  