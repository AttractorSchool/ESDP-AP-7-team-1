from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from accounts.models import Account

from applications.models import Application
from applications.services.statuses import set_application_status


class CreateStudent(View):

    def post(self, request, *args, **kwargs):
        data = {}
        application = get_object_or_404(Application, pk=kwargs.get('pk'))
        if Account.objects.filter(email=application.email).exists():
            data['email'] = 'Пользователь с такой почтой уже существует'
            return JsonResponse(data)
        if Account.objects.filter(phone_number=application.phone).exists():
            data['phone'] = 'Пользователь с таким номером телефона уже существует'
            return JsonResponse(data)
        student = Account.objects.create(first_name=application.applicant_name, last_name=application.applicant_surname,
                                         email=application.email, phone_number=application.phone,
                                         application=application)
        student.set_password('1234')
        student.save()
        student.groups.add(2)
        set_application_status(application=application, status_name='Завершена', author=request.user)
        data['success'] = 'Студент создан'
        return JsonResponse(data)
