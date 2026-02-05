from django.urls import path
from restaurants import views

urlpatterns = [
    path('get-all/', views.get_all_responses, name='get all restaurants'),
    path('get/<str:restaurant_id>', views.get_one_response, name='get one restaurant'),
    path('create/', views.create_restaurant_item, name='create restaurant'),
    path('update/<str:restaurant_id>', views.update_restaurant, name='update_restaurant'),
    path('delete/<str:restaurant_id>', views.delete_restaurant, name='delete_restaurant'),
    path('contact/',views.send_email, name='contact restaurant'),
]