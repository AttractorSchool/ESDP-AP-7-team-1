from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import Group
from django.urls import reverse
from django.views.generic import CreateView

from accounts.forms.register_form import SignUpForm
from accounts.models.account import Account


class RegisterView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    template_name = 'register.html'
    form_class = SignUpForm
    

    def post(self, request, *args, **kwargs):
        create_user =  super(RegisterView, self).post(request, *args, **kwargs)
        group_pk = self.kwargs.get("pk")
        group = Group.objects.get(name=group_pk)
        user = Account.objects.get(pk=self.object.pk)
        user.groups.add(group)
        return create_user


    def get_success_url(self):
        user = self.object
        return reverse('profile', kwargs={'pk': user.pk})

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='admin').exists()
