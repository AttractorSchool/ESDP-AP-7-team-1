from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, View

from accounts.models import Account

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject_name: str = self.get_object().subject.name
        teachers = Account.objects.filter(groups__name='teacher', teach_subjects__name=subject_name)
        context['teachers'] = teachers

        return context

    def get_success_url(self):
        return reverse('groupings')


def remove_teacher_from_grouping_view(request, pk):
    grouping: Grouping = get_object_or_404(Grouping, pk=pk)
    teacher_grouping: TeacherGrouping = grouping.teacher_groupings.last()
    finished_at = request.POST.get('finished_at')
    teacher_grouping.finished_at = finished_at
    teacher_grouping.is_active = False
    teacher_grouping.save()
    return redirect('grouping_update', pk=pk)


def add_teacher_to_grouping_view(request, grouping_pk):
    grouping: Grouping = get_object_or_404(Grouping, pk=grouping_pk)
    teacher_pk: str = request.POST.get('teacher_pk')
    teacher: Account = get_object_or_404(Account, pk=teacher_pk)
    started_at: str = request.POST.get('started_at')
    TeacherGrouping.objects.create(grouping=grouping, teacher=teacher, started_at=started_at)
    return redirect('grouping_update', pk=grouping_pk)


class DelGroupingView(View):
    def post(self, *args, **kwargs):
        grouping = get_object_or_404(Grouping, pk=kwargs['pk'])
        grouping.is_deleted = True
        grouping.save()
        return redirect('groupings')
