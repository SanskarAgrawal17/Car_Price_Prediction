from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from carapp.models import *
import random
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import HttpResponse
from carapp.models import NewUser
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password  # Import check_password
from django.shortcuts import render
from .forms import CarInputForm
from .ml_model import CarPricePredictionModel  # Import your prediction model class
import numpy as np
from forex_python.converter import CurrencyRates
from decimal import Decimal
# Define the exchange rate for USD to INR (you can update this as needed)

def wellcome(request):
    return render(request, 'index.html')

def signin(request):
    value = None

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Hash the user's password
        hashed_password = make_password(password)

        try:
            newuser = NewUser.objects.create(username=username, email=email, password=hashed_password)
            newuser.save()
            value = 3  # User created successfully
            request.session['username']=newuser.username
        except IntegrityError as e:
            if 'UNIQUE constraint failed: carapp_newuser.email' in str(e):
                value = 2  # Email already exists
            else:
                value = 1
                
    else:
        return render(request, 'signin.html')

    context = {'value': value}
    return render(request, 'signin.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = NewUser.objects.get(username=username)
            if check_password(password, user.password):
                # Password matches
                request.session['username'] = user.username
                res = render(request, 'home.html')
            else:
                # Password doesn't match
                LoginError = "Invalid Username or Password.."
                res = render(request, 'login.html', {'LoginError': LoginError})
        except NewUser.DoesNotExist:
            # User not found
            LoginError = "Invalid Username or Password.."
            res = render(request, 'login.html', {'LoginError': LoginError})
    else:
        if 'username' in request.session.keys():
            res = render(request, 'home.html')
        else:
            res = render(request, 'login.html')
    return res


def home(request):
    if 'username'  in  request.session.keys():
        return render(request,'home.html')
    else:
        return HttpResponseRedirect('/login')


     
            







def predict_price(request):
    if 'username'  in  request.session.keys():
        if request.method == 'POST':
            form = CarInputForm(request.POST)
            if form.is_valid():
                

                # Create an instance of your model
                model_file_path = 'Models\Car_Price_Model.pkl'
                model = CarPricePredictionModel(model_file_path)

                input_data = {
                    'year': form.cleaned_data['year'],
                    'present_price': form.cleaned_data['present_price'],  # Use the converted value
                    'kilometer_driven': form.cleaned_data['kilometer_driven'],
                    'fuel_type': form.cleaned_data['fuel_type'],
                    'seller_type': form.cleaned_data['seller_type'],
                    'transmission': form.cleaned_data['transmission'],
                }

            

                
                

                input_data = np.array([
                    input_data['year'],
                    input_data['present_price'],
                    input_data['kilometer_driven'],
                    input_data['fuel_type'],
                    input_data['seller_type'],
                    input_data['transmission']
                ], dtype=object).reshape(1, 6)

                estimated_price = model.predict(input_data)[0]

                # If USD is chosen, convert the estimated price to USD
                
                formatted_price = "{:.4f}".format(estimated_price)
                currency_symbol = '₹'

                return render(request, 'predict_price.html', {'form': form, 'estimated_price': formatted_price, 'currency_symbol': currency_symbol})
        else:
            form = CarInputForm()

        return render(request, 'predict_price.html', {'form': form})


    else:
        return HttpResponseRedirect('/login')
def members(request):
    if 'username'  in  request.session.keys():
        return render(request,'members.html')
    else:
        return HttpResponseRedirect('/login')


def logout(request):
    if 'username'  in  request.session.keys():
        request.session.pop('username')
    return HttpResponseRedirect('/')
