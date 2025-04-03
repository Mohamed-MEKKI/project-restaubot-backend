from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from menuitem.models import MenuItem
from menuitem.serializers import MenuItemSerializer


@api_view(['GET'])
def get_all_responses(request):
    serialized_data = MenuItemSerializer(MenuItem.objects.all(), many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_one_response(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, id=menu_item_id)
    serialized_data = MenuItemSerializer(menu_item)
    return Response(serialized_data.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_menu_item(request):
    serialized_data = MenuItemSerializer(data=request.data)

    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)

    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_menu_item(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, id=menu_item_id)
    serialized_data = MenuItemSerializer(menu_item, data=request.data)

    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_menu_item(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, id=menu_item_id)
    menu_item.delete()
    return Response({"message": "Menu item deleted successfully"}, status=status.HTTP_200_OK)
