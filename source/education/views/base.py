from django.views.generic import TemplateView

from applications.forms.application_form import ApplicationSendForm


class IndexView(TemplateView):
    template_name = 'index.html'
    form = ApplicationSendForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form}
        return self.render_to_response(context)
