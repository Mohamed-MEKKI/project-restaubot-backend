from django.urls import path
from menuitem import views

urlpatterns = [
    path('get-all/', views.get_all_responses, name='get all restaurants'),
    path('get/<str:restaurant_id>', views.get_one_response, name='get one restaurant'),
    path('create/', views.create_menu_item, name='create restaurant'),
    path('update/<str:restaurant_id>', views.update_menu_item, name='update_restaurant'),
    path('item/<int:restaurant_id>/delete/', views.delete_menu_item, name='delete_restaurant'),
]