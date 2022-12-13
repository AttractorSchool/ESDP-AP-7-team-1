from django.views.generic import ListView

from education.forms.change_application_status_form import ApplicationStatusChangeForm
from education.models import Application


class ShowApplicationsView(ListView):
    model = Application
    template_name = 'show_applications.html'
    context_object_name = 'applications'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowApplicationsView, self).get_context_data(**kwargs)
        context['form'] = ApplicationStatusChangeForm
        return context

