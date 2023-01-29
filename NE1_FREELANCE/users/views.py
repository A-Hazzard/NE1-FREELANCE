from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from home.models import *
from searchResults.models import *

def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['user_name']
        password = request.POST['password']

        print("\nEmail:", email, "\nUsername:", username ,"\nPassword:", password, "\n")
        user = authenticate(request, email=email, password=password)
    
        if user is not None:
            login(request, user)
            print("\nSuccessfully logged in\n")
            return redirect('search_jobs')
        else:
            messages.success(request, ("Invalid Email/Password"))
            print("\nInvalid Email/Password\n")
            return redirect('home_page')




    else:
        return render(request, 'searchResults/search_results.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Logged out"))
    return redirect("home_page")

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            user = authenticate(email=email, username=username, password=password)

            login(request, user)

            messages.success(request, ("Registered Successfull"))  
            return redirect("home_page")


    else:
        form = UserCreationForm()
        services = Service.objects.all()
        job_category = JobCategory.objects.all()
    
        context = {
                'services' : services, 
                'job_category': job_category,
                'form':form
            }
        return render(request, 'home/index.html', context)
