# from django import forms

# from education.models import Application, Status


# class ApplicationStatusChangeForm(forms.ModelForm):
#     statuses = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='',
#                                               required=True, queryset=Status.objects.all())

#     class Meta:
#         model = Application
#         fields = ('statuses',)
