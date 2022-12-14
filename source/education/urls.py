from django.urls import path

from education.views.base import IndexView, NotificationView
from education.views.crm_view import CrmView
from education.views.schedule import StudentScheduleView, GroupingsScheduleView
from education.views.subjects import SubjectListView, SubjectAddView, SubjectEditView, DelSubjectView
from education.views.applications import ApplicationListView, ApplicationEditView, DeleteApplicationView, \
    ApplicationDetailView, ApplicationCustomEditView, ApplicationContractEditView, ApplicationPayedEditView, ApplicationRejectView
from education.views.packages import PackageListView, PackageAddView, PackageEditView, DelPackageView
from education.views.discounts import DiscountListView, DiscountAddView, DiscountEditView, DelDiscountView
from education.views.groupings import GroupingListView, GroupingAddView, GroupingEditView, DelGroupingView
from education.views.contracts import open_contract_pdf, send_contract

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('notification/', NotificationView.as_view(), name='notification'),
    path('crm/', CrmView.as_view(), name='crm'),
    path('schedule/', StudentScheduleView.as_view(), name='schedule_student'),
    path('schedule-groupings/', GroupingsScheduleView.as_view(), name='schedule_groupings'),
    path('subjects/', SubjectListView.as_view(), name='subjects'),
    path('subject_add/', SubjectAddView.as_view(), name='subject_add'),
    path('subject_update/<int:pk>', SubjectEditView.as_view(), name='subject_update'),
    path('subject_del/<int:pk>', DelSubjectView.as_view(), name='subject_del'),
    path('application_update/<int:pk>', ApplicationEditView.as_view(), name='application_update'),

    path('application-custom-update/<int:pk>', ApplicationCustomEditView.as_view(), name='application_custom_update'),
    path('application-contract-update/<int:pk>', ApplicationContractEditView.as_view(), name='application_contract_update'),
    path('application-payed-update/<int:pk>', ApplicationPayedEditView.as_view(), name='application_payed_update'),
    path('application-reject/<int:pk>', ApplicationRejectView.as_view(), name='application_reject'),

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
    path('groupings/', GroupingListView.as_view(), name='groupings'),
    path('grouping_add/', GroupingAddView.as_view(), name='grouping_add'),
    path('grouping_update/<int:pk>', GroupingEditView.as_view(), name='grouping_update'),
    path('grouping_del/<int:pk>', DelGroupingView.as_view(), name='grouping_del'),
    
    path('open_contract/<int:pk>',open_contract_pdf,name='open_contract'),
    path('send_contract/<int:pk>', send_contract, name='send_contract' ),
]
