from django.urls import path

from accounts.views.admin_register_view import AdminRegisterView
from accounts.views.login_view import LoginView
from accounts.views.logout_view import logout_view
from accounts.views.profile_view import ProfileView
from accounts.views.student_register_view import StudentRegisterView
from accounts.views.teacher_register_view import TeacherRegisterView

urlpatterns = [
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('register_teacher/', TeacherRegisterView.as_view(), name='register_teacher'),
    path('register_student/', StudentRegisterView.as_view(), name='register_student'),
    path('register_admin/', AdminRegisterView.as_view(), name='register_admin'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
