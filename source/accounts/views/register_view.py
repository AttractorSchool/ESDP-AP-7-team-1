from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import Group
from django.urls import reverse
from django.views.generic import CreateView

from accounts.forms.register_form import SignUpForm


class RegisterView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    template_name = 'register.html'
    form_class = SignUpForm

    def get_success_url(self):
        user = self.object
        # group = Group.objects.get(name='admin')
        # user.groups.add(group)
        return reverse('profile', {'pk': self.object.pk})

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='admin').exists()
