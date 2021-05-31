from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone

from django.contrib.auth.decorators import login_required

from .models import Resume, Vacancy


def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def placeResume(request):
    if request.method == 'POST':
        author = request.user
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        speciality = request.POST.get('speciality')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        about = request.POST.get('about')
        experience = request.POST.get('experience')
        date = timezone.now()

        resume = Resume(author=author, date_of_birth=date_of_birth, gender=gender,
                        specialty=speciality, city=city, phone=phone,
                        desc=about, experience=experience, date=date)
        resume.save()
        return redirect('index')

    return render(request, 'place-resume.html')


@login_required(login_url='login')
def placeVacancy(request):
    if request.method == 'POST':
        employer = request.user
        company = request.POST.get('company')
        position = request.POST.get('position')
        salary = request.POST.get('salary')
        desc = request.POST.get('desc')
        adress = request.POST.get('adress')
        contact = request.POST.get('contact')
        date = timezone.now()

        vacancy = Vacancy(employer=employer, company=company, position=position, salary=salary,
                          desc=desc, adress=adress, contact=contact, date=date)
        vacancy.save()
        return redirect('index')

    return render(request, 'place-vacancy.html')


def seeVacancies(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        vacancies = Vacancy.objects.filter(position__contains=search)

    else:
        vacancies = Vacancy.objects.order_by('-date')

    context = {
        'title': 'vacancies',
        'content': vacancies
    }
    return render(request, 'see.html', context)


def seeResumes(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        resumes = Resume.objects.filter(specialty__contains=search)

    else:
        resumes = Resume.objects.order_by('-date')

    context = {
        'title': 'resumes',
        'content': resumes
    }
    return render(request, 'see.html', context)


def detailResume(request, id):
    resume = Resume.objects.get(id=id)

    context = {
        'resume': resume
    }
    return render(request, 'detail-resume.html', context)


def detailVacancy(request, id):
    vacancy = Vacancy.objects.get(id=id)

    context = {
        'vacancy': vacancy
    }
    return render(request, 'detail-vacancy.html', context)
