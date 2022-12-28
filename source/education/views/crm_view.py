from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class CrmView(LoginRequiredMixin, TemplateView):
    template_name = 'crm.html'
