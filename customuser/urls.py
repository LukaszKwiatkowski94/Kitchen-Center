from django.urls import path
from customuser.views import register_view, edit_profile_view, profile_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('edit_profile/', edit_profile_view, name='edit_profile'),
    path('profile/', profile_view, name='profile'),
]