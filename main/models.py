from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    specialty = models.CharField('Speciality', max_length=70)
    date_of_birth = models.DateField('Date of birth', null=True)
    gender = models.CharField('Gender', max_length=6, choices=GENDERS)
    city = models.CharField('City', max_length=50)
    phone = models.CharField('Phone number', max_length=20)
    desc = models.TextField('About')
    experience = models.IntegerField('Years of experience')
    date = models.DateTimeField('Date of placing')

    def __str__(self):
        return f'{self.author.username} - {self.specialty}'


class Vacancy(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField('Company name', max_length=100)
    position = models.CharField('Position', max_length=70)
    salary = models.TextField('Salary', default='Salary not specified')
    desc = models.TextField('Description')
    adress = models.CharField('Adress of company', max_length=70)
    contact = models.CharField('Contact data', max_length=100)
    date = models.DateTimeField('Date of placing')

    def __str__(self):
        return f'{self.company} is looking for {self.position}'
