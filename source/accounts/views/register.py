from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import CreateView
from accounts.forms.register_form import AccountCreationForm


class RegisterView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    template_name = 'register.html'
    form_class = AccountCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()
