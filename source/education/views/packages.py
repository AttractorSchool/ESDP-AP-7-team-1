from django.views.generic import View, ListView, CreateView, UpdateView
from education.models import Packet
from education.forms.package_form import PackageForm
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404


class PackageListView(ListView):
    template_name = 'education/packages.html'
    model = Packet
    context_object_name = 'packages'

    def get_queryset(self, *args, **kwargs):
        return Packet.objects.filter(is_deleted=False).order_by('pk')



class PackageAddView(CreateView):
    template_name = 'education/package_add.html'
    form_class = PackageForm
    model = Packet

    def get_success_url(self):
        return reverse('packages')



class PackageEditView(UpdateView):
    template_name = 'education/package_update.html'
    model = Packet
    form_class = PackageForm
    context_object_name = 'package'

    def get_success_url(self):
        return reverse('packages')


    
class DelPackageView(View):
    def post(self, *args, **kwargs):
        package = get_object_or_404(Packet, pk=kwargs['pk'])
        package.is_deleted = True
        package.save()
        return redirect('packages')

