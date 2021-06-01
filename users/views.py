from main.models import Resume
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import login, logout

from django.contrib import messages

from django.core.exceptions import ObjectDoesNotExist


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = first_name + last_name

        u = User(first_name=first_name, last_name=last_name, email=email, password=password, username=username)
        u.save()

        return redirect('login')
    return render(request, 'register.html')


def logIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            u = User.objects.get(email=email, password=password)
            login(request, u)
            return redirect('index')
        except ObjectDoesNotExist:
            messages.info(request, 'Email or password is incorrect!')

    return render(request, 'login.html')


def logOut(request):
    logout(request)
    return redirect('login')


def profile(request):
    user = request.user

    try:
        resume = Resume.objects.get(author=user)
    except ObjectDoesNotExist:
        return redirect('place-resume')

    context = {
        'u': user,
        'r': resume
    }
    return render(request, 'profile.html', context)
