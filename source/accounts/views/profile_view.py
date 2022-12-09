from django.views.generic import DetailView

from accounts.models import Account


class ProfileView(DetailView):
    template_name = 'profile_board.html'
    model = Account
