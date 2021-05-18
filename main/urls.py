from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('place-resume/', views.placeResume, name='place-resume'),
    path('place-vacancy/', views.placeVacancy, name='place-vacancy'),
    path('see-vacancies/', views.seeVacancies, name='see-offers'),
    path('see-resumes/', views.seeResumes, name='see-resumes')
]
