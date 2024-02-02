from django import forms
from .models import SalaryPrediction

class SalaryPredictionForm(forms.ModelForm):
    class Meta:
        model = SalaryPrediction
        fields = ['YearsExperience']
