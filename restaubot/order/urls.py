from django.urls import path
from order import views

urlpatterns = [
    path('get-all/', views.get_all_responses, name='get all orders'),
    path('get/<str:phone_number>', views.get_one_response, name='get one response'),
    path('get_one_item/<str:order_id>', views.get_one_order, name='get one order'),
    path('create/', views.create_order, name='create order'),
    path('update/<str:order_id>', views.update_order, name='update order'),
    path('update_status/<str:order_id>', views.update_order_status, name='update order status'),
    path('delete/<str:order_id>', views.delete_order, name='delete order'),
    path('delete_order_chatbot/<str:phone_number>', views.delete_order_in_chatbot, name='delete order chatbot'),
    path('delete/', views.delete_all_orders, name='delete all orders'),
]