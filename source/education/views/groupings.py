from django.views.generic import View, ListView, CreateView, UpdateView
from education.models import Grouping
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from education.forms.grouping_form import GroupingForm



class GroupingListView(ListView):
    template_name = 'education/groupings.html'
    model = Grouping
    context_object_name = 'groupings'


    def get_queryset(self, *args, **kwargs):
        return Grouping.objects.filter(is_deleted = False).order_by('-pk')



class GroupingAddView(CreateView):
    template_name = 'education/grouping_add.html'
    model = Grouping
    form_class = GroupingForm


    def get_success_url(self):
        return reverse('groupings')



class GroupingEditView(UpdateView):
    template_name = 'education/grouping_update.html'
    model = Grouping
    form_class = GroupingForm
    context_object_name = 'grouping'

    def get_success_url(self):
        return reverse('groupings')



class DelGroupingView(View):
    def post(self, *args, **kwargs):
        grouping = get_object_or_404(Grouping, pk=kwargs['pk'])
        grouping.is_deleted = True
        grouping.save()
        return redirect('groupings')