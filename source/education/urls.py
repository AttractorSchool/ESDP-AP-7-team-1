from django.urls import path
from education.views.base import IndexView
from education.views.change_application_status_view import ChangeStatusView
from education.views.schedule import StudentScheduleView, GroupingsScheduleView
from education.views.subjects import SubjectListView, SubjectAddView, SubjectEditView, DelSubjectView
from education.views.applications import ApplicationListView, ApplicationEditView, DeleteApplicationView, ApplicationDetailView
from education.views.packages import PackageListView, PackageAddView, PackageEditView, DelPackageView
from education.views.discounts import DiscountListView, DiscountAddView, DiscountEditView, DelDiscountView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('schedule/', StudentScheduleView.as_view(), name='schedule_student'),
    path('schedule-groupings/', GroupingsScheduleView.as_view(), name='schedule_groupings'),
    path('change/status/<int:pk>', ChangeStatusView.as_view(), name='change_status'),
    path('subjects/', SubjectListView.as_view(), name='subjects'),
    path('subject_add/', SubjectAddView.as_view(), name='subject_add'),
    path('subject_update/<int:pk>', SubjectEditView.as_view(), name='subject_update'),
    path('subject_del/<int:pk>', DelSubjectView.as_view(), name='subject_del'),
    path('application_update/<int:pk>', ApplicationEditView.as_view(), name='application_update'),
    path('application_delete/<int:pk>', DeleteApplicationView.as_view(), name='application_delete'),
    path('applications/', ApplicationListView.as_view(), name='applications'),
    path('applications/<int:pk>/detail', ApplicationDetailView.as_view(), name='application_detail'),
    path('packages/', PackageListView.as_view(), name='packages'),
    path('package_add/', PackageAddView.as_view(), name='package_add'),
    path('package_update/<int:pk>', PackageEditView.as_view(), name='package_update'),
    path('package_del/<int:pk>', DelPackageView.as_view(), name='package_del'),
    path('discounts/', DiscountListView.as_view(), name='discounts'),
    path('discount_add/', DiscountAddView.as_view(), name='discount_add'),
    path('discount_update/<int:pk>', DiscountEditView.as_view(), name='discount_update'),
    path('discount_del/<int:pk>', DelDiscountView.as_view(), name='discount_del'),
]
