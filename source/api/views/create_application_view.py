import json
import re

from django.http import JsonResponse
from django.views import View

import phonenumbers

from applications.models import Application


class AddApplicationView(View):
    def post(self, request, *args, **kwargs):
        data = {}
        if request.body:
            application = json.loads(request.body)
            email = application.get('email')
            phone = application.get('phone')
            surname = application.get('surname')
            name = application.get('name')
            subjects = application.get('subjects')
            if email == '':
                data['error'] = 'Укажите почту'
                data['id'] = 'email_error'
            else:
                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                if re.fullmatch(regex, email):
                    if phone == '':
                        data['error'] = 'Укажите корректный телефон'
                        data['id'] = 'phone_error'
                    else:
                        check_number = phonenumbers.parse(phone, "KZ")
                        if phonenumbers.is_valid_number(check_number):
                            if name == '':
                                data['error'] = 'Укажите имя'
                                data['id'] = 'name_error'
                            else:
                                if surname == '':
                                    data['error'] = 'Укажите фамилию'
                                    data['id'] = 'surname_error'
                                else:
                                    if len(subjects) == 0:
                                        data['error'] = 'Выберете предмет'
                                        data['id'] = 'subject_error'
                                    else:
                                        application_create = Application.objects.create(applicant_name=name,
                                                                                        applicant_surname=surname,
                                                                                        email=email, phone=phone)
                                        for i in subjects:
                                            application_create.subjects.add(i)
                                        application_create.statuses.add(1)
                                        data['success'] = 'Заявка создана'
                        else:
                            data['success'] = 'Укажите корректный телефон'
                else:
                    data['success'] = 'Укажите корректную почту'
        return JsonResponse(data)
