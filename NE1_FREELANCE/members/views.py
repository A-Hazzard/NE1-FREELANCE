from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):

    if request.method == 'POST':
        print("\nLogin Form Submitted\n")
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        #check if user has entered all input fields
        if user is not None:
            login(request, user)
            print("\nLogin Success\n")
            return redirect('home_page')
        else:
            messages.success(request, "Invalid Email/Password")
            print("\nInvalid Email/Password\n")
            return redirect("login")

    else:
        print("\nVisited Login Page. Waiting for POST...\n")
        return render(request, 'members/login.html', {})

