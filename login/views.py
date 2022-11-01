from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.


def login_(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/feed/')
        return render(request, 'login/login.html')
    else:
        return redirect('/feed/')


def logout_(request):
    logout(request)
    return redirect('/')


def registration(request):
    if not request.user.is_authenticated:
        username_msg = ""
        email_msg = ""
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            avatar = request.FILES['avatar']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            user_valid_check = User.objects.filter(username=username).exists()
            email_valid_check = User.objects.filter(email=email).exists()
            if user_valid_check:
                username_msg = "User name already exist, please choose new one."
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                profile = Profile.objects.create(user=user,avatar=avatar)
                if profile:
                    return redirect('/')
        return render(request, 'login/registration.html', {'umsg': username_msg, 'email_msg': email_msg})
    else:
        return redirect('/feed/')
