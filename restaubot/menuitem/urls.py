from django.urls import path
from menuitem import views

urlpatterns = [
    path('get-all/', views.get_all_responses, name='get_menu_items'),
    path('get/<str:menu_item_id>', views.get_one_response, name='get_one_menu_item'),
    path('create/', views.create_menu_item, name='create_menu_items'),
    path('update/<str:menu_item_id>', views.update_menu_item, name='update_menu_items'),
    path('item/<int:menu_item_id>/delete/', views.delete_menu_item, name='delete_menu_items'),
]