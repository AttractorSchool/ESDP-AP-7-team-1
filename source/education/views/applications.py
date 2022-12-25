from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView, View

from education.forms.application_edit_form import (ApplicationContractEditForm,
                                                   ApplicationCustomEditForm,
                                                   ApplicationPayedEditForm,
                                                   ApplicationRejectForm)
from education.models import Application, ApplicationStatus, Status
from education.services.statuses import (get_button_status,
                                         set_application_status)


class ApplicationListView(TemplateView):
    template_name = 'education/applications.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sorted_by: str | None = self.request.GET.get('sorted')
        queryset = Application.objects.filter(is_deleted=False)
        if sorted_by == 'status':
            query: str = """
                    SELECT T2.APPLICATION_ID AS "id"
                    FROM EDUCATION_APPLICATIONSTATUS,
                        EDUCATION_STATUS,

                        (SELECT EDUCATION_APPLICATIONSTATUS.APPLICATION_ID AS "application_id",
                                MAX(EDUCATION_APPLICATIONSTATUS.CREATED_AT) AS "created_at"
                            FROM EDUCATION_APPLICATIONSTATUS
                            GROUP BY EDUCATION_APPLICATIONSTATUS.APPLICATION_ID) AS T2
                    WHERE EDUCATION_APPLICATIONSTATUS.APPLICATION_ID = T2.APPLICATION_ID
                        AND EDUCATION_APPLICATIONSTATUS.CREATED_AT = T2.CREATED_AT
                        AND EDUCATION_APPLICATIONSTATUS.STATUS_ID = EDUCATION_STATUS.ID
                    ORDER BY EDUCATION_STATUS.NAME
                    """
            queryset = Application.objects.raw(query)
        elif sorted_by == '-status':
            query: str = """
                    SELECT T2.APPLICATION_ID AS "id"
                    FROM EDUCATION_APPLICATIONSTATUS,
                        EDUCATION_STATUS,

                        (SELECT EDUCATION_APPLICATIONSTATUS.APPLICATION_ID AS "application_id",
                                MAX(EDUCATION_APPLICATIONSTATUS.CREATED_AT) AS "created_at"
                            FROM EDUCATION_APPLICATIONSTATUS
                            GROUP BY EDUCATION_APPLICATIONSTATUS.APPLICATION_ID) AS T2
                    WHERE EDUCATION_APPLICATIONSTATUS.APPLICATION_ID = T2.APPLICATION_ID
                        AND EDUCATION_APPLICATIONSTATUS.CREATED_AT = T2.CREATED_AT
                        AND EDUCATION_APPLICATIONSTATUS.STATUS_ID = EDUCATION_STATUS.ID
                    ORDER BY EDUCATION_STATUS.NAME desc
                    """
            queryset = Application.objects.raw(query)
        elif sorted_by is not None:
            queryset = queryset.order_by(sorted_by)
        context['applications'] = queryset
        context['sorted_by'] = sorted_by
        return context


class ApplicationEditView(TemplateView):
    """Формирование контекста для отображения шаблона редактирования заявки"""

    template_name = 'education/application_update.html'

    def get_context_data(self, **kwargs):
        context = super(ApplicationEditView, self).get_context_data(**kwargs)
        application = get_object_or_404(Application, pk=kwargs['pk'])
        context['application'] = application
        application_custom_form = ApplicationCustomEditForm(instance=application)
        application_contract_form = ApplicationContractEditForm(instance=application)
        application_payed_form = ApplicationPayedEditForm(instance=application)
        application_reject_form = ApplicationRejectForm(instance=application)
        context['application_custom_form'] = application_custom_form
        context['application_contract_form'] = application_contract_form
        context['application_payed_form'] = application_payed_form
        context['application_reject_form'] = application_reject_form
        button_status: dict[str, str] = get_button_status(application=application)

        context.update(button_status)
        return context


class ApplicationCustomEditView(View):
    """Редактирование основных полей заявки с установкой соответствующего статуса"""

    def post(self, *args, **kwargs):
        application = get_object_or_404(Application, pk=kwargs['pk'])
        form = ApplicationCustomEditForm(data=self.request.POST, instance=application)
        if form.is_valid():
            form.save()
        required_fields = list(application.__dict__.values())[2:19]
        if None not in required_fields:
            status_name = 'Подписание договора'
            set_application_status(application=application, status_name=status_name, author=self.request.user)
        else:
            status_name = 'В работе'
            set_application_status(application=application, status_name=status_name, author=self.request.user)
        return HttpResponseRedirect(reverse_lazy('application_update', kwargs={'pk': self.kwargs['pk']}))


class ApplicationContractEditView(View):
    """Редактирование поля договор заявки с установкой соответствующего статуса"""

    def post(self, *args, **kwargs):
        application = get_object_or_404(Application, pk=kwargs['pk'])
        form = ApplicationContractEditForm(self.request.POST, self.request.FILES, instance=application)
        if form.is_valid():
            form.save()
        if application.contract == '':
            status_name = 'Подписание договора'
        else:
            status_name = 'Ожидание оплаты'
        set_application_status(application=application, status_name=status_name, author=self.request.user)
        return HttpResponseRedirect(reverse_lazy('application_update', kwargs={'pk': self.kwargs['pk']}))


class ApplicationPayedEditView(View):
    """Редактирование поля оплаты заявки с установкой соответствующего статуса"""

    def post(self, *args, **kwargs):
        application = get_object_or_404(Application, pk=kwargs['pk'])
        form = ApplicationPayedEditForm(self.request.POST, self.request.FILES, instance=application)
        if form.is_valid():
            form.save()
        if application.payed is True:
            status_name = 'Оплачена'
        else:
            status_name = 'Ожидание оплаты'
        set_application_status(application=application, status_name=status_name, author=self.request.user)
        return HttpResponseRedirect(reverse_lazy('application_update', kwargs={'pk': self.kwargs['pk']}))


class ApplicationRejectView(View):
    """Установка статуса Отклонена"""

    def post(self, *args, **kwargs):
        application = get_object_or_404(Application, pk=kwargs['pk'])
        status = get_object_or_404(Status, name='Отклонена')
        author = self.request.user
        form = ApplicationRejectForm(self.request.POST)
        application_status: ApplicationStatus = form.save(commit=False)
        application_status.application = application
        application_status.status = status
        application_status.author = author
        application_status.save()

        return HttpResponseRedirect(reverse_lazy('application_update', kwargs={'pk': self.kwargs['pk']}))


class DeleteApplicationView(View):
    def post(self, *args, **kwargs):
        subject = get_object_or_404(Application, pk=kwargs['pk'])
        subject.is_deleted = True
        subject.save()
        return redirect('applications')


class ApplicationDetailView(DetailView):
    model = Application
    template_name = "education/application_detail.html"
