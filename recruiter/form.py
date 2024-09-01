from django import forms
from .models import Job
from allauth.account.forms import SignupForm

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
