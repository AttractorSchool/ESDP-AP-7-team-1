from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from accounts.models import Account
from education.models import Application


class CreateUser(View):

    def post(self, request, *args, **kwargs):
        data = {}
        application = get_object_or_404(Application, pk=kwargs.get('pk'))
        if Account.objects.filter(email=application.email).exists():
            data['email'] = 'Пользователь с такой почтой уже существует'
            return JsonResponse(data)
        if Account.objects.filter(phone_number=application.phone).exists():
            data['phone'] = 'Пользователь с таким номером телефона уже существует'
            return JsonResponse(data)
        a = Account.objects.create(first_name=application.applicant_name, last_name=application.applicant_surname,
                                   email=application.email, phone_number=application.phone)
        a.set_password('1234')
        a.save()
        a.groups.add(2)
        data['success'] = 'Студент создан'
        return JsonResponse(data)
