from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from accounts.models import Account


class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_user.html'
    model = Account
    success_url = reverse_lazy('main')
