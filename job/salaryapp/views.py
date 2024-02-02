from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import pickle
# Create your views here.
# views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

# views.py

from django.shortcuts import render, redirect

def registration(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        name = request.POST.get('name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        experience = request.POST.get('experience')
        designation = request.POST.get('designation')

        # Process the form data (you can add additional logic here)
        
        # Redirect to a success page
        return render(request, 'login.html')

    return render(request, 'register.html')



from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Simulate user authentication without a database
        if email == 'test@example.com' and password == 'password':
            # For simplicity, hardcoding a single user for demonstration
            # In a real-world scenario, you might implement a more secure mechanism
            user = {
                'email': email,
                'username': 'testuser',
            }

            # Store user information in session
            request.session['user'] = user

            # Redirect to a success page or dashboard
            return render(request, 'home.html', {'user': user})
        else:
            # Display an error message (you can customize this part)
            error_message = "Invalid email or password. Please try again."

    return render(request, 'login.html', {'error_message': error_message if 'error_message' in locals() else None})



# Import necessary libraries and classes
from django.shortcuts import render
from .forms import SalaryPredictionForm
import pickle

# Define the path to the trained model
MODEL_PATH = '/home/jiji/salary/salaryapp/static/css/images/salary_prediction_model.pkl'

def make_prediction(YearsExperience):
    # Load the trained model
    model = pickle.load(open(MODEL_PATH, 'rb'))
    
    # Make a prediction using the loaded model
    prediction = model.predict([[YearsExperience]])

    return prediction[0]

def predict_salary(request):
    # Create an instance of the SalaryPredictionForm
    form = SalaryPredictionForm(request.POST or None)

    # Check if the form is submitted and valid
    if request.method == 'POST' and form.is_valid():
        # Get input values from the form
        YearsExperience = form.cleaned_data['YearsExperience']
        
        # Make a prediction using the loaded model
        prediction = make_prediction(YearsExperience)

        # Save the prediction to the database
        instance = form.save(commit=False)
        instance.Salary = prediction
        instance.save()

        # Render the results page with the prediction
        return render(request, 'result.html', {'prediction': f'The predicted salary is: ${round(prediction, 2)}'})

    # Render the details page with the form
    return render(request, 'details.html', {'form': form})
