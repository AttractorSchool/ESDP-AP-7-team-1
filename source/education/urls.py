from django.urls import path
from education.views.base import IndexView
from education.views.change_application_status_view import ChangeStatusView
from education.views.schedule import StudentScheduleView, GroupingsScheduleView
from education.views.show_applications_view import ShowApplicationsView
from education.views.subjects import SubjectListView, SubjectAddView, SubjectEditView, DelSubjectView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('schedule/', StudentScheduleView.as_view(), name='schedule_student'),
    path('schedule-groupings/', GroupingsScheduleView.as_view(), name='schedule_groupings'),
    path('applications/', ShowApplicationsView.as_view(), name='show_applications'),
    path('change/status/<int:pk>', ChangeStatusView.as_view(), name='change_status'),
    path('subjects/', SubjectListView.as_view(), name='subjects'),
    path('subject_add/', SubjectAddView.as_view(), name='subject_add'),
    path('subject_update/<int:pk>', SubjectEditView.as_view(), name='subject_update'),
    path('subject_del/<int:pk>', DelSubjectView.as_view(), name='subject_del')
]
