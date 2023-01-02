from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView

from education.forms.schedule_create import ScheduleForm
from education.models import Auditorium, Grouping, Schedule, ClassTime


class StudentScheduleView(ListView):
    '''для вывода расписания залогиневшегося студента'''
    template_name = 'education/student_schedule.html'
    model = Schedule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        groupings = user.groupings.all()
        context['monday'] = []
        context['tuesday'] = []
        context['wednesday'] = []
        context['thursday'] = []
        context['friday'] = []
        context['saturday'] = []
        for grouping in groupings:
            for schedule in grouping.schedules.all():
                context[schedule.week_day].append((grouping, schedule.class_time))
        return context


class GroupingsScheduleView(ListView):
    template_name = 'education/groupings_schedule.html'
    model = Schedule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        groupings = Grouping.objects.all()
        list_groupings = []
        for grouping in groupings:
            week_days = [grouping.name, '', '', '', '', '', '']
            for schedule in grouping.schedules.all():
                if schedule.week_day == 'monday':
                    week_days[1] = schedule.class_time
                elif schedule.week_day == 'tuesday':
                    week_days[2] = schedule.class_time
                elif schedule.week_day == 'wednesday':
                    week_days[3] = schedule.class_time
                elif schedule.week_day == 'thursday':
                    week_days[4] = schedule.class_time
                elif schedule.week_day == 'friday':
                    week_days[5] = schedule.class_time
                elif schedule.week_day == 'saturday':
                    week_days[6] = schedule.class_time
            list_groupings.append(week_days)
        context['list_groupings'] = list_groupings
        return context


class ScheduleCreateView(CreateView):
    template_name = 'education/schedule_create.html'
    model = Schedule
    form_class = ScheduleForm

    def get_success_url(self):
        return reverse('crm')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # schedule = Schedule.objects.all(is_deleted=False)
        # context['schedule'] = schedule
        auditoriums = Auditorium.objects.all()
        sum_dict = {'108': {}, '109': {}, '110': {}}
        for auditorium in auditoriums:
            schedules = auditorium.schedules.filter(is_deleted=False)
            my_dict = {'monday': {}, 'tuesday': {}, 'wednesday': {}, 'thursday': {}, 'friday': {}, 'saturday': {}}
            for schedule in schedules:
                my_dict[schedule.week_day][schedule.class_time.number_lesson] = schedule.grouping.name
            sum_dict[auditorium.name] = my_dict
        context['sum_dict'] = sum_dict
        groupings = Grouping.objects.all()
        context['groupings'] = groupings
        return context

    def post(self, request, *args, **kwargs):
        form = ScheduleForm(request.POST)
        auditorium_pk = request.POST.get('auditorium')
        auditorium = get_object_or_404(Auditorium, pk=auditorium_pk)
        week_day = request.POST.get('week_day')
        class_time_pk = request.POST.get('class_time')
        class_time = get_object_or_404(ClassTime, pk=class_time_pk)
        
        if Schedule.objects.filter(auditorium=auditorium, class_time=class_time,
                                   week_day=week_day, is_deleted=False).exists():
            schedule = get_object_or_404(Schedule, auditorium=auditorium, class_time=class_time,
                                         week_day=week_day, is_deleted=False)
            schedule.is_deleted = True
            schedule.save()
        if form.is_valid():
            grouping = request.POST.get('grouping')
            if grouping:
                form.save()
        return redirect('schedule_create')
