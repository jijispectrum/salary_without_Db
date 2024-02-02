from django.db import models

# Create your models here.
from django.db import models

class SalaryPrediction(models.Model):
    YearsExperience= models.FloatField()
    Salary = models.FloatField(null=True, blank=True)
