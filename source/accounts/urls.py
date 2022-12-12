from django.urls import path

from accounts.views.login_view import LoginView
from accounts.views.logout_view import logout_view
from accounts.views.profile_view import ProfileView
from accounts.views.register import RegisterView
from accounts.views.delete_view import UserDeleteView

urlpatterns = [
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path("account/<int:pk>/delete/", UserDeleteView.as_view(), name= "user_delete"),
    path("account/<int:pk>/confirm_delete/", UserDeleteView.as_view(), name= "confirm_user_delete")
]
