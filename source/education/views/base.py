from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from education.forms.application_form import ApplicationSendForm
from education.models import Status, ApplicationStatus

class IndexView(TemplateView):
    template_name = 'index.html'
    form = ApplicationSendForm

    def get(self, request, *args, **kwargs):
        context = {'form': self.form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            application = form.save()
            status_name = 'Создана'
            status = get_object_or_404(Status, name=status_name)
            application_status = ApplicationStatus(application=application, status=status)
            application_status.save()
            return redirect('notification')
            
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class NotificationView(TemplateView):
    template_name = 'education/notification.html'
