from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = first_name + last_name

        u = User(first_name=first_name, last_name=last_name, email=email, password=password, username=username)
        u.save()

        return redirect('index')

    else:
        return render(request, 'register.html')


def logIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        u = User.objects.get(email=email, password=password)

        if u is not None:
            login(request, u)
            return redirect('index')

    return render(request, 'login.html')


def logOut(request):
    logout(request)
    return redirect('login')