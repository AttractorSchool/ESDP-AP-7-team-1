from django.urls import path
from accounts.views.base import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
]
