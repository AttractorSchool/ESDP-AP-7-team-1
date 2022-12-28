from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.views.generic import CreateView

from accounts.forms.register_form import SignUpForm


class RegisterView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    template_name = 'register.html'
    form_class = SignUpForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            group_pk = self.kwargs.get("pk")
            group = Group.objects.get(name=group_pk)
            user.groups.add(group)
            return redirect('crm')
        context = {'form': form}
        return self.render_to_response(context)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='admin').exists()
