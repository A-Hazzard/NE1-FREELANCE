from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError

from .models import User
from .models import Service

from searchResults.models import JobCategory

import datetime


# Create your views here.
def index(request):
    services = Service.objects.all()
    job_category = JobCategory.objects.all()

    # search_jobs(request)
    return render(request,'home/index.html' , {'services' : services, 'job_category': job_category})

def register(request):
    services = Service.objects.all()
    job_category = JobCategory.objects.all()
    
    context_jobs = {
                'services' : services, 
                'job_category': job_category,
            }
    context_email_already_taken = {
                'services' : services, 
                'job_category': job_category,
                "email_already_taken" : "Email already taken"
            }

    context_blank_field_error = {
                'services' : services, 
                'job_category': job_category,
                "blank_field_error" : "Don't leave any fields blank"
            }
        
    context_common_password = {
                'services' : services, 
                'job_category': job_category,
                "common_password" : "Password is too common, choose a different one"
            }

    context_common_password = {
                'services' : services, 
                'job_category': job_category,
                "password_validation" : "Password must have at least 1 upper case letter, 1 lower case letter, 1 number, and 1 character"
            }

    registered = {
        'services' : services, 
            'job_category': job_category,
                'registered' : 'Registered Successfully'
    }


    if request.method == 'POST':

        # Get form data
        username = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']

        # Check if fields are filled in
        if not all([username, email, password]):
            messages.error(request, "Don't leave any fields blank")
            print("\nDon't leave any fields blank\n")

            return render(request, 'home/index.html', context_blank_field_error)

        # Check if username is taken
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
            print("\nEmail already taken\n")
            return render(request, 'home/index.html', context_email_already_taken)

        # Check if password is common
        common_passwords = ["password", "12345", "admin"]

        if password in common_passwords:
            messages.error(request, "Password is too common, choose a different one")
            print("\nPassword is too common, choose a different one\n")
            return render(request, 'home/index.html', context_common_password)

        # Check if password has at least 1 upper case letter, 1 lower case letter, 1 number, and 1 character
        if not any(i.isupper() for i in password) or not any(i.islower() for i in password) or not any(i.isdigit() for i in password) or not any(i.isalpha() for i in password):
            messages.error(request, "Password must have at least 1 upper case letter, 1 lower case letter, 1 number, and 1 character")
            print("\nPassword must have at least 1 upper case letter, 1 lower case letter, 1 number, and 1 character\n")
            return render(request, 'home/index.html', registered)

        # Create user object
        # Hash the password
        hashed_password = make_password(password)
        try:
            user = User(email=email, username=username, password=hashed_password)
            user.save()
            messages.success(request, "Signup successful")
            print("\n", __file__, "\nRegistered Successfully!\n")


            return render(request, 'searchResults/search_results.html', context_jobs)
        except IntegrityError as e:
            print("\n", __file__, "\nRegistered Unsuccessful!\n")
            
            return render(request, 'home/index.html', context_jobs)
    else:

        return render(request, 'searchResults/search_results.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                # login successful
                # do something
                print("checked password")
            else:
                # login failed
                print("hmm")
                # do something
        except User.DoesNotExist:
            # user with email not found
            # do something
            print("Exception ocurred")
    else:
        return render(request, 'home/index.html')
