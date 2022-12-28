from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import TemplateView

from accounts.forms.login_form import LoginForm
from accounts.models import Account


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        password = form.cleaned_data.get('password')
        if '@' not in form.cleaned_data.get('email'):
            phone = form.cleaned_data.get('email')
            email = Account.objects.filter(phone_number=phone).values('email')
            if len(email) == 0:
                return redirect('login')
            email_str = email[0]
            user = authenticate(request, email=email_str.get('email'), password=password)
            if not user:
                return redirect('login')
            login(request, user)
            return redirect('crm')
        email = form.cleaned_data.get('email')
        user = authenticate(request, email=email, password=password)
        if not user:
            return redirect('login')
        login(request, user)
        return redirect('crm')
