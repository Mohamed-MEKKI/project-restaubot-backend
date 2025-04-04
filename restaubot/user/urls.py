from django.urls import path
from user import views

urlpatterns = [
    path('get-all/', views.get_all_responses, name='get users'),
    path('get/<str:user_id>', views.get_one_response, name='get one user'),
    path('create/', views.create_user, name='create user'),
    path('update/<str:user_id>', views.update_user, name='update user'),
    path('item/<int:user_id>/delete/', views.delete_user, name='delete user'),
]