from django.views.generic import ListView
from education.models import Schedule


class ScheduleView(ListView):
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
