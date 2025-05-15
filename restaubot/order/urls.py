from django.urls import path
from order import views

urlpatterns = [
    path('get-all/', views.get_all_responses, name='get all orders'),
    path('get/<str:order_id>', views.get_one_response, name='get one order'),
    path('create/', views.create_order, name='create order'),
    path('update/<str:order_id>', views.update_order, name='update_order'),
    path('item/<int:order_id>/delete/', views.delete_order, name='delete_order'),
]