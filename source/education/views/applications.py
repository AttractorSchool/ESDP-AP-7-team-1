from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, View

from education.forms.application_edit_form import ApplicationEditForm
from education.forms.change_application_status_form import ApplicationStatusChangeForm
from education.models import Application


class ApplicationListView(ListView):
    template_name = 'education/applications.html'
    model = Application
    context_object_name = 'applications'

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(is_deleted=False)


class ApplicationEditView(UpdateView):
    template_name = 'education/application_update.html'
    model = Application
    form_class = ApplicationEditForm
    context_object_name = 'application'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ApplicationEditView, self).get_context_data(**kwargs)
        context['status_form'] = ApplicationStatusChangeForm
        return context

    def get_success_url(self):
        return reverse_lazy('application_update', kwargs={'pk': self.kwargs['pk']})


class DeleteApplicationView(View):
    def post(self, *args, **kwargs):
        subject = get_object_or_404(Application, pk=kwargs['pk'])
        subject.is_deleted = True
        subject.save()
        return redirect('applications')


class ApplicationDetailView(DetailView):
    model = Application
    template_name = "education/application_detail.html"
