from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.views.generic import CreateView

from accounts.forms.register_form import SignUpForm
from accounts.forms.teacher_registerform import TeacherSignUpForm
from accounts.models.account import TeacherInformation


class RegisterView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    template_name = 'register.html'
    form_class = SignUpForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher_form'] = TeacherSignUpForm
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form_teacher = TeacherSignUpForm(request.POST)
        group_pk = self.kwargs.get("pk")
        group = Group.objects.get(name=group_pk)
        if form.is_valid():
            if 'teacher' in request.path:
                if form_teacher.is_valid():
                    user = form.save()
                    user.groups.add(group)
                    teacher = TeacherInformation.objects.create(user=user,
                                                                birth_date=form_teacher.cleaned_data['birth_date'],
                                                                teacher_inn=form_teacher.cleaned_data['teacher_inn'],
                                                                address=form_teacher.cleaned_data['address'],
                                                                education=form_teacher.cleaned_data['education'],
                                                                )
                    teacher.save()
                    teacher.subjects.set(form_teacher.cleaned_data['subjects'])
                    return redirect('crm')
                else:
                    context = {'form': form, 'teacher_form': form_teacher}
                    return self.render_to_response(context)
            user = form.save()
            user.groups.add(group)
            return redirect('crm')
        context = {'form': form, 'teacher_form': form_teacher}
        return self.render_to_response(context)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='admin').exists()
