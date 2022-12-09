from django.urls import path

from education.views.base import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
]
