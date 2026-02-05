from django.urls import path
from user import views

urlpatterns = [
    path('get-all/', views.get_all_users, name='get users'),
    path('get/<str:user_id>', views.get_user, name='get one user'),
    path('create/', views.create_user, name='create user'),
    path('update/<str:user_id>', views.update_user, name='update user'),
    path('delete/<str:user_id>', views.delete_user, name='delete user'),
    path('delete/', views.delete_all_users, name='delete all user'),
]