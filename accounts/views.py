from django import forms
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login as dj_login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm

# Create your views here.

# def index(request):
#     return render(request, 'accounts/index.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created! You are now able to log in..')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form':form})
    

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if user is not None:
                dj_login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return redirect('index')
            # if form is not valid
        else:
            messages.info(request, f'Invalid username or password!')
            return render(request, "accounts/login.html", context= {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, "accounts/login.html", context= {'form': form})

def logout_user(request):
    logout(request)
    messages.info(request, f'Logged out successfully!')
    return redirect('index')
