from django.shortcuts import render, redirect
from .models import Service
from searchResults.models import JobCategory
# from searchResults.views import search_jobs
from django.contrib import messages
from django.contrib.auth.models import User

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
            return render(request, 'home/index.html')

        # Check if username is taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            print("\nUsername already taken\n")
            return render(request, 'home/index.html')

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
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Signup successful")
        print("\nSignup successful\n")
        return render(request, 'searchResults/search_results.html')


    else:
        return render(request, 'searchResults/search_results.html')