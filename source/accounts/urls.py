from django.urls import path

from accounts.views.profile_view import ProfileView
from accounts.views.register import RegisterView

urlpatterns = [
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
]
