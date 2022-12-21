from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, View

from education.forms.application_edit_form import ApplicationEditForm
# from education.forms.change_application_status_form import ApplicationStatusChangeForm
from education.models import Application, ApplicationStatus, Status
from education.services.statuses import set_application_status


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

    def form_valid(self, form) -> HttpResponse:
        super().form_valid(form)
        application: Application = self.get_object()

        # print(self.get_object().__dict__)
        # print('*' * 50)

        required_fields = list(application.__dict__.values())[2:19]
        print(required_fields)
        
        if None not in required_fields:
            status_name = 'Подписание договора'
            print(status_name)
            set_application_status(application=application, status_name=status_name, author=self.request.user)
        else:
            status_name = 'В работе'
            set_application_status(application=application, status_name=status_name, author=self.request.user)

        if application.contract is True:
            status_name = 'Ожидание оплаты'
            set_application_status(application=application, status_name=status_name, author=self.request.user)

        if application.payed is True:
            status_name = 'Оплачено'
            set_application_status(application=application, status_name=status_name, author=self.request.user)

        if application.student is not None:
            status_name = 'Завершена'
            set_application_status(application=application, status_name=status_name, author=self.request.user)

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ApplicationEditView, self).get_context_data(**kwargs)
        # context['status_form'] = ApplicationStatusChangeForm
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
