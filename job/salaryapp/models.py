from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class SalaryPrediction(models.Model):
    YearsExperience= models.FloatField()
    Salary = models.FloatField(null=True, blank=True)
# models.py
from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    dob = models.DateField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    experience = models.FloatField()
    designation = models.CharField(max_length=255)
