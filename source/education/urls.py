from django.urls import path

from education.views.base import IndexView
from education.views.schedule import ScheduleView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
]
