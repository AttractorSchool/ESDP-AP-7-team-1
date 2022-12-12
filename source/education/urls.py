from django.urls import path

from education.views.base import IndexView
from education.views.schedule import StudentScheduleView, GroupingsScheduleView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('schedule/', StudentScheduleView.as_view(), name='schedule'),
    path('schedule-groupings/', GroupingsScheduleView.as_view(), name='schedule_groupings'),

]
