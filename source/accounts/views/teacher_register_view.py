from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.urls import reverse
from django.views.generic import CreateView
from accounts.forms.register_form import SignUpForm


class TeacherRegisterView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    template_name = 'register_teacher.html'
    form_class = SignUpForm

    def get_success_url(self):
        user = self.object
        group = Group.objects.get(name='teacher')
        user.groups.add(group)
        return reverse('main')

    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()
