from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
# yourproject/urls.py

from django.contrib import admin
from .models import SalaryPrediction

# Register the SalaryPrediction model
admin.site.register(SalaryPrediction)
