from django import forms
from .models import SalaryPrediction

class SalaryPredictionForm(forms.ModelForm):
    class Meta:
        model = SalaryPrediction
        fields = ['YearsExperience']
# forms.py
from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
