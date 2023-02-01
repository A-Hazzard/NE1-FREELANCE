from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import RegisterUserForm

def login_user(request):
    print("visited\n\n")
    if request.method == 'POST':
        print("\nLogin Form Submitted\n")
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        #check if user has entered all input fields
        if user is not None:
            login(request, user)
            print("\nLogin Success\n")
            return redirect('search_jobs')
        else:
            messages.success(request, "Invalid Email/Password")
            print("\nInvalid Email/Password\n")
            return redirect("login")

    else:
        print("\nVisited Login Page. Waiting for POST...\n")
        return render(request, "members/login.html", {})

def logout_user(request):
    logout(request)

    messages.success(request, ("Logged out Successfully"))

    return redirect('home_page')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)


        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            user = authenticate(username = username, password = password)

            login(request, user)
            messages.success(request, ("Registration Successful"))

            return redirect("search_jobs")
    
    else:
        form = RegisterUserForm()
    return render(request, 'members/signup.html', {'form': form})