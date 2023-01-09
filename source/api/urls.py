from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from api.views.create_application_view import AddApplicationView
from api.views.create_student_by_application_view import CreateStudent
from api.views.sum_package_view import SumPackageView, SumDiscountView

urlpatterns = [
    path('get_sum', csrf_exempt(SumPackageView.as_view()), name='sum_package'),
    path('get_discount', csrf_exempt(SumDiscountView.as_view()), name='sum_discount'),
    path('create-application', csrf_exempt(AddApplicationView.as_view()), name='add_application_api'),
    path('create-student-by-application/<int:pk>', CreateStudent.as_view(), name='Create_student_by_application'),
]
