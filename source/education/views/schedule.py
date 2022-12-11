from django.views.generic import ListView
from education.models import Schedule


class ScheduleView(ListView):
    template_name = 'education/student_schedule.html'
    model = Schedule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        classes = user.classes.all()
        context['monday'] = []
        context['tuesday'] = []
        context['wednesday'] = []
        context['thursday'] = []
        context['friday'] = []
        context['saturday'] = []
        for klass in classes:
            for schedule in klass.schedules.all():
                context[schedule.week_day].append((klass, schedule.time_start))
        print(context)
        return context
