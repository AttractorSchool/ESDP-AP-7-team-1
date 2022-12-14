from django.shortcuts import redirect
from django.views.generic import TemplateView

from education.forms.application_form import ApplicationSendForm


class ApplicationView(TemplateView):
    template_name = 'application.html'
    form = ApplicationSendForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        context = {}
        context['form'] = form
        return self.render_to_response(context)