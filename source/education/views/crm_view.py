from django.views.generic import TemplateView


class CrmView(TemplateView):
    template_name = 'crm.html'
