from django.views.generic import ListView
from education.models import Schedule, Grouping


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
                context[schedule.week_day].append((grouping, schedule.time_start))
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
                    week_days[1] = schedule.time_start
                elif schedule.week_day == 'tuesday':
                    week_days[2] = schedule.time_start
                elif schedule.week_day == 'wednesday':
                    week_days[3] = schedule.time_start
                elif schedule.week_day == 'thursday':
                    week_days[4] = schedule.time_start
                elif schedule.week_day == 'friday':
                    week_days[5] = schedule.time_start
                elif schedule.week_day == 'saturday':
                    week_days[6] = schedule.time_start
            list_groupings.append(week_days)
        context['list_groupings'] = list_groupings
        return context

