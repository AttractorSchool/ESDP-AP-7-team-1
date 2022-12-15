from django.views.generic import View, ListView, UpdateView
from education.models import Application
from education.forms.application_form import ApplicationSendForm
from education.forms.application_edit_form import ApplicationEditForm
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView


class ApplicationListView(ListView):
    template_name = 'education/applications.html'
    model = Application
    context_object_name = 'applications' 

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(is_deleted=False).order_by('created_at')



class ApplicationEditView(UpdateView):
    template_name = 'education/application_update.html'
    model = Application
    form_class = ApplicationEditForm
    context_object_name = 'application'

    def get_success_url(self):
        return reverse('applications')


class DeleteApplicationView(View):
    def post(self, *args, **kwargs):
        subject = get_object_or_404(Application, pk=kwargs['pk'])
        subject.is_deleted = True
        subject.save()
        return redirect('applications')


class ApplicationDetailView(DetailView):
    model = Application
    template_name = "education/application_detail.html"