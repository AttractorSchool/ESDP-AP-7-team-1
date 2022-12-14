from django.urls import path
from accounts.views.application import ApplicationView
from education.views.base import IndexView
from education.views.change_application_status_view import ChangeStatusView
from education.views.schedule import StudentScheduleView, GroupingsScheduleView
from education.views.show_applications_view import ShowApplicationsView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('application/', ApplicationView.as_view(), name='application'),
    path('schedule/', StudentScheduleView.as_view(), name='schedule_student'),
    path('schedule-groupings/', GroupingsScheduleView.as_view(), name='schedule_groupings'),
    path('applications/', ShowApplicationsView.as_view(), name='show_applications'),
    path('change/status/<int:pk>', ChangeStatusView.as_view(), name='change_status')

]
