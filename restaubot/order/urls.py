from django.urls import path
from menuitem import views

urlpatterns = [
    path('get-all/', views.get_all_responses, name='get all orders'),
    path('get/<str:order_id>', views.get_one_response, name='get one order'),
    path('create/', views.create_menu_item, name='create_menu_items'),
    path('update/<str:order_id>', views.update_menu_item, name='update order'),
    path('item/<int:order_id>/delete/', views.delete_menu_item, name='delete order'),
]