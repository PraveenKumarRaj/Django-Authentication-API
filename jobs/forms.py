from django import forms

from .models import Jobs, Application


class JobForm(forms.ModelForm):

    class Meta:
        model = Jobs
        fields = ['title', 'description', 'num_workers']


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ['aadhaar_id', 'age', 'experience']
        