from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from .forms import ProfileForm, RegisterUserForm, UpdateUserProfileForm
from .models import Profile

def login_user(request):
    print("\nLogin Visited")

    if request.user.is_authenticated: #if user is logged in redirect them
        return redirect('search_jobs')

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
            print("\nInvalid Username/Password\n")
            return redirect("login")

    else:
        print("\nVisited Login Page. Waiting for POST...\n")
        return render(request, "members/login.html", {})

def logout_user(request):
    logout(request)

    messages.success(request, ("Logged out Successfully"))

    return redirect('home_page')

def register_user(request):
    if request.user.is_authenticated: # if user is logged in redirect them
        return redirect('search_jobs')

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            profile = Profile.objects.create(user=user)
            profile.save()

            login(request, user)
            messages.success(request, "Registration Successful")

            return redirect("search_jobs")
        else:
            messages.success(request, "Registration Failed")
    else:
        form = RegisterUserForm()
    return render(request, 'members/signup.html', {'form': form})



def user_profile(request):
    if request.user.is_authenticated:
        user = request.user.profile
        userAccount = request.user
        userEmail = request.user.email

        form = ProfileForm(instance=user)
        update_user_form = UpdateUserProfileForm(instance=user)

        print('\nUsername:', userAccount, '\nEmail:', userEmail, '\n')

        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=user)
            update_user_form = UpdateUserProfileForm(request.POST, instance=user)

            if (form.errors):
                print('\n\nForm errors: ', form.errors, '\n\n')

            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                
            if (update_user_form.errors):
                print('\n\nForm errors: ', update_user_form.errors, '\n\n')

            if update_user_form.is_valid():
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                email = request.POST.get('email')
                password = request.POST.get('password1')

                if password:
                    userAccount.set_password(password)
                    update_session_auth_hash(request, userAccount)

                if first_name:
                    userAccount.first_name = first_name
                    print('\nUpdated' + first_name + ' successfully\n')

                if last_name:
                    userAccount.last_name = last_name
                    print('\nUpdated' + last_name + ' successfully\n')
                
                if email:
                    userAccount.email = email
                    print('\nUpdated' + email + ' successfully\n')

                userAccount.save()


        context = {
            'user': user,
            'userEmail': userEmail,
            'form': form,
            'update_user_form': update_user_form,
        }
        return render(request, 'members/profile.html', context)
    else:
        return redirect('home_page')

