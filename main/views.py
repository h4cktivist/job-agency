from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')


def placeResume(request):
    return HttpResponse('Place Resume')


def seeOffers(request):
    return HttpResponse('See Offers')


def registerWorkplace(request):
    return HttpResponse('Register Workplace')
