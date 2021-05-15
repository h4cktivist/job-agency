from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('place-resume/', views.placeResume, name='place-resume'),
    path('see-vacancies/', views.seeVacancies, name='see-offers'),
    path('register-workplace/', views.placeVacancy, name='place-vacancy'),
]
