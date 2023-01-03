from django.urls import path

from applications.views import (ApplicationContractEditView,
                                ApplicationCustomEditView,
                                ApplicationDetailView, ApplicationEditView,
                                ApplicationListView, ApplicationPayedEditView,
                                ApplicationRejectView, DeleteApplicationView)

urlpatterns = [
    path('update/<int:pk>', ApplicationEditView.as_view(), name='application_update'),
    path('custom-update/<int:pk>', ApplicationCustomEditView.as_view(), name='application_custom_update'),
    path(
        'contract-update/<int:pk>',
        ApplicationContractEditView.as_view(),
        name='application_contract_update',
        ),
    path('payed-update/<int:pk>', ApplicationPayedEditView.as_view(), name='application_payed_update'),
    path('reject/<int:pk>', ApplicationRejectView.as_view(), name='application_reject'),

    path('delete/<int:pk>', DeleteApplicationView.as_view(), name='application_delete'),
    path('', ApplicationListView.as_view(), name='applications'),
    path('detail/<int:pk>', ApplicationDetailView.as_view(), name='application_detail'),
]
