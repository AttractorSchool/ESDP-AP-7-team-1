from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView
from education.models import Subject
from education.forms.subject_form import SubjectForm
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404


class SubjectListView(ListView):
    template_name = 'education/subjects.html'
    model = Subject
    context_object_name = 'subjects' 

    def get_queryset(self, *args, **kwargs):
        return Subject.objects.filter(is_deleted=False).order_by('name')



class SubjectAddView(CreateView):
    template_name = 'education/subject_add.html'
    form_class = SubjectForm
    model = Subject

    def get_success_url(self):
        return reverse('subjects')


class SubjectEditView(UpdateView):
    template_name = 'education/subject_update.html'
    model = Subject
    form_class = SubjectForm
    context_object_name = 'subject'

    def get_success_url(self):
        return reverse('subjects')


class DelSubjectView(View):
    def post(self, *args, **kwargs):
        subject = get_object_or_404(Subject, pk=kwargs['pk'])
        subject.is_deleted = True
        subject.save()
        return redirect('subjects')


   