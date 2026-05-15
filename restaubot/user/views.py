from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from user.models import User
from user.serializers import UserSerializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_users(request):
    """Get all users - requires authentication"""
    serialized_data = UserSerializers(User.objects.all(), many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request, user_id):
    """Get a specific user - requires authentication"""
    user = get_object_or_404(User, id=user_id)
    serialized_data = UserSerializers(user)
    return Response(serialized_data.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user(request):
    """Create a user - requires authentication"""
    serialized_data = UserSerializers(data=request.data)

    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)

    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request, user_id):
    """Update a user - requires authentication.
    Users can only update their own profile.
    """
    user = get_object_or_404(User, id=user_id)
    
    # Check if user is updating their own profile or is admin
    if request.user.user_id != user_id and not request.user.is_staff:
        return Response(
            {"detail": "You do not have permission to update this user."},
            status=status.HTTP_403_FORBIDDEN
        )
    
    serialized_data = UserSerializers(user, data=request.data)

    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(user_id):
    """Delete a user - requires authentication and admin privileges"""
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_all_users():
    """Delete all users - requires authentication and admin privileges"""
    users = User.objects.all()
    if not users:
        return Response({"message": "No users to delete"}, status=status.HTTP_404_NOT_FOUND)
    users.delete()
    return Response({"message": "All users deleted successfully"}, status=status.HTTP_204_NO_CONTENT)  