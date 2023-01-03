from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, View

from education.forms.grouping_form import GroupingForm
from education.models import Grouping, TeacherGrouping


class GroupingListView(ListView):
    template_name = 'education/groupings.html'
    model = Grouping
    context_object_name = 'groupings'

    def get_queryset(self, *args, **kwargs):
        return Grouping.objects.filter(is_deleted=False).order_by('-pk')


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


def remove_teacher_from_grouping(request, pk):
    grouping: Grouping = get_object_or_404(Grouping, pk=pk)
    teacher_grouping: TeacherGrouping = grouping.teacher_groupings.last()
    finished_at = request.POST.get('finished_at')
    teacher_grouping.finished_at = finished_at
    teacher_grouping.is_active = False
    teacher_grouping.save()
    return redirect('grouping_update', pk=pk)


class DelGroupingView(View):
    def post(self, *args, **kwargs):
        grouping = get_object_or_404(Grouping, pk=kwargs['pk'])
        grouping.is_deleted = True
        grouping.save()
        return redirect('groupings')
