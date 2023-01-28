from django.shortcuts import render, redirect
from .models import Service
from searchResults.models import JobCategory
from django.contrib import messages
from .models import User
import datetime
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError

# Create your views here.
def index(request):
    services = Service.objects.all()
    job_category = JobCategory.objects.all()

    # search_jobs(request)
    return render(request,'home/index.html' , {'services' : services, 'job_category': job_category})

def register(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']

        
        # Check if fields are filled in
        if not all([username, email, password]):
            messages.error(request, "Don't leave any fields blank")
            print("\nDon't leave any fields blank\n")
            error = {
                "blank_field_error" : "Don't leave any fields blank"
            }
            return render(request, 'home/index.html', error)

        # Check if username is taken
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
            print("\nEmail already taken\n")
            error = {
                "signup_error" : "Email Already Taken"
            }
            return render(request, 'home/index.html', error)

        # Check if password is common
        common_passwords = ["password", "12345", "admin"]
        if password in common_passwords:
            messages.error(request, "Password is too common, choose a different one")
            print("\nPassword is too common, choose a different one\n")
            return render(request, 'home/index.html')

        # Check if password has at least 1 upper case letter, 1 lower case letter, 1 number, and 1 character
        if not any(i.isupper() for i in password) or not any(i.islower() for i in password) or not any(i.isdigit() for i in password) or not any(i.isalpha() for i in password):
            messages.error(request, "Password must have at least 1 upper case letter, 1 lower case letter, 1 number, and 1 character")
            print("\nPassword must have at least 1 upper case letter, 1 lower case letter, 1 number, and 1 character\n")
            return render(request, 'home/index.html')

        # Create user object
        # Hash the password
        hashed_password = make_password(password)
        try:
            user = User(email=email, username=username, password=hashed_password)
            user.save()
            messages.success(request, "Signup successful")
            print("\n", __file__, "\nRegistered Successfully!\n")
            return render(request, 'searchResults/search_results.html')
        except IntegrityError as e:
            print("\n", __file__, "\nRegistered Unsuccessful!\n")
            error = {
                "signup_error" : "Email Already Taken"
            }
            return render(request, 'home/index.html', error)
    else:
        return render(request, 'searchResults/search_results.html')

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
