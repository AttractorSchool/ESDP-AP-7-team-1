from django.urls import path

from education.views.base import IndexView
from education.views.contracts import open_contract_pdf, send_contract
from education.views.crm_view import CrmView
from education.views.discounts import (DelDiscountView, DiscountAddView,
                                       DiscountEditView, DiscountListView)
from education.views.groupings import (DelGroupingView, GroupingAddView,
                                       GroupingEditView, GroupingListView, remove_teacher_from_grouping)
from education.views.packages import (DelPackageView, PackageAddView,
                                      PackageEditView, PackageListView)
from education.views.schedule import (GroupingsScheduleView,
                                      ScheduleCreateView, StudentScheduleView,
                                      schedule_generate_view)
from education.views.subjects import (DelSubjectView, SubjectAddView,
                                      SubjectEditView, SubjectListView)

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('crm/', CrmView.as_view(), name='crm'),

    path('schedule/', StudentScheduleView.as_view(), name='schedule_student'),
    path('schedule/', StudentScheduleView.as_view(), name='schedule_student'),
    path('schedule-groupings/', GroupingsScheduleView.as_view(), name='schedule_groupings'),
    path('schedule-create/', ScheduleCreateView.as_view(), name='schedule_create'),
    path('schedule-generate/', schedule_generate_view, name='schedule_generate'),

    path('subjects/', SubjectListView.as_view(), name='subjects'),
    path('subject_add/', SubjectAddView.as_view(), name='subject_add'),
    path('subject_update/<int:pk>', SubjectEditView.as_view(), name='subject_update'),
    path('subject_del/<int:pk>', DelSubjectView.as_view(), name='subject_del'),

    path('packages/', PackageListView.as_view(), name='packages'),
    path('package_add/', PackageAddView.as_view(), name='package_add'),
    path('package_update/<int:pk>', PackageEditView.as_view(), name='package_update'),
    path('package_del/<int:pk>', DelPackageView.as_view(), name='package_del'),
    path('discounts/', DiscountListView.as_view(), name='discounts'),
    path('discount_add/', DiscountAddView.as_view(), name='discount_add'),
    path('discount_update/<int:pk>', DiscountEditView.as_view(), name='discount_update'),
    path('discount_del/<int:pk>', DelDiscountView.as_view(), name='discount_del'),

    path('groupings/', GroupingListView.as_view(), name='groupings'),
    path('groupings/remove-teacher/<int:pk>', remove_teacher_from_grouping, name='remove_teacher_from_grouping'),
    path('grouping_add/', GroupingAddView.as_view(), name='grouping_add'),
    path('grouping_update/<int:pk>', GroupingEditView.as_view(), name='grouping_update'),
    path('grouping_del/<int:pk>', DelGroupingView.as_view(), name='grouping_del'),

    path('open_contract/<int:pk>', open_contract_pdf, name='open_contract'),
    path('send_contract/<int:pk>', send_contract, name='send_contract'),
]
