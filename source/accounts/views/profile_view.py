from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from accounts.models import Account


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'profile_board.html'
    model = Account
