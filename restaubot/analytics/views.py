import json
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from menuitem.models import MenuItem
from order.models import Order

@api_view(['GET'])
def get_menus_orders_stats(request):
    # fetch orders belonging to the given user id
    menu_items = MenuItem.objects.filter(user_id=request.user)
    count_menus = menu_items.count()
    orders = Order.objects.filter(user_id=request.user)
    count_orders = orders.count()
    count_customers = orders.values('customer').distinct().count() if count_orders else 0
    revenue_agg = orders.aggregate(total_revenue=Sum('total'))
    count_revenue = revenue_agg.get('total_revenue') or 0

    return Response({
        "total_menus": count_menus,
        "count_orders": count_orders,
        "count_customers": count_customers,
        "count_revenue": count_revenue
    }, status=status.HTTP_200_OK)