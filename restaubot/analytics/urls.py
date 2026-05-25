from django.urls import path
from analytics import views

urlpatterns = [
    path('get_menus_orders_stats/', views.get_menus_orders_stats, name='get menus and orders stats'),
]