from django.contrib.auth import get_user_model, update_session_auth_hash
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView

from accounts.forms.change_form import UserChangeForm
from django.urls import reverse


class AccountChangeView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('account_detail', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        return HttpResponseRedirect(self.get_success_url())
