from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView

from education.forms.application_form import ApplicationSendForm


class IndexView(TemplateView):
    template_name = 'index.html'
    form = ApplicationSendForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        print(form.errors)
        context = {}
        context['form'] = form

        return self.render_to_response(context)
