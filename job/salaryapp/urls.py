# urls.py

from django.urls import path
from .views import home,registration,login,predict_salary,make_prediction

urlpatterns = [
    path('', home, name='home'),
    path('register/', registration, name='registration'),
    path('login/', login, name='login'),
    path('details/', predict_salary, name='predict_salary'),
    path('results/',make_prediction, name='make_prediction'),
    
    # Add other URL patterns for your application if needed
]
