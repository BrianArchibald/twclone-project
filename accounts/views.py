from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # User wants an account
    else:
        #user wants to enter info
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    #TODO need to route to homepage
    return render(request, 'accounts/signup.html')