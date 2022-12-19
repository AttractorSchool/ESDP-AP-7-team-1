from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import Account


class TestGroupingsScheduleView(TestCase):

    def test_schedule_list_get(self):
        client = Client()

        response = client.get(reverse('schedule_groupings'))

        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'education/groupings_schedule.html')


class TestStudentScheduleView(TestCase):

    def test_schedule_list_get(self):
        student = Account.objects.create(
            phone_number='+77774441122',
            password='123asdf',
        )
        client = Client()
        client.force_login(student)

        response = client.get(reverse('schedule_student'))

        self.assertAlmostEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'education/student_schedule.html')
