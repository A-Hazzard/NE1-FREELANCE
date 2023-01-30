from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
        return redirect("login")

def logout_user(request):
    logout(request)

    messages.success(request, ("Logged out Successfully"))

    return redirect('home_page')

def register_user(request):

    return redirect('home_page')