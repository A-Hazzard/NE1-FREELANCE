from django.shortcuts import render, redirect
from .models import Service
from searchResults.models import JobCategory
from django.contrib import messages
from .models import User
import datetime

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
            return render(request, 'home/index.html')

        # Check if username is taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return render(request, 'home/index.html')

        # Check if password is common
        common_passwords = ["password", "12345", "admin"]
        if password in common_passwords:
            messages.error(request, "Password is too common, choose a different one")
            return render(request, 'home/index.html')

        # Check if password has at least 1 upper case letter, 1 lower case letter, 1 number, and 1 character
        if not any(i.isupper() for i in password) or not any(i.islower() for i in password) or not any(i.isdigit() for i in password) or not any(i.isalpha() for i in password):
            messages.error(request, "Password must have at least 1 upper case letter, 1 lower case letter, 1 number, and 1 character")
            return render(request, 'home/index.html')

        # Create user object
        user = User.objects.create(email=email,username=username, password=password,last_login=datetime.datetime.now(),date_joined=datetime.datetime.now())
        user.save()

        messages.success(request, "Signup successful")
        
        return render(request, 'searchResults/search_results.html')
    else:
        return render(request, 'searchResults/search_results.html')