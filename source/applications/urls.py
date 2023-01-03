from django.urls import path

from applications.views import (ApplicationContractEditView,
                                ApplicationCustomEditView,
                                ApplicationDetailView, ApplicationEditView,
                                ApplicationListView, ApplicationPayedEditView,
                                ApplicationRejectView, DeleteApplicationView)

urlpatterns = [
    path('application_update/<int:pk>', ApplicationEditView.as_view(), name='application_update'),
    path('application-custom-update/<int:pk>', ApplicationCustomEditView.as_view(), name='application_custom_update'),
    path(
        'application-contract-update/<int:pk>',
        ApplicationContractEditView.as_view(),
        name='application_contract_update',
        ),
    path('application-payed-update/<int:pk>', ApplicationPayedEditView.as_view(), name='application_payed_update'),
    path('application-reject/<int:pk>', ApplicationRejectView.as_view(), name='application_reject'),

    path('application_delete/<int:pk>', DeleteApplicationView.as_view(), name='application_delete'),
    path('applications/', ApplicationListView.as_view(), name='applications'),
    path('applications/<int:pk>/detail', ApplicationDetailView.as_view(), name='application_detail'),
]
