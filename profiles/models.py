# models.py
from django.db import models
from django.conf import settings
import csv

class Questions(models.Model):
    class Meta:
        
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
   
    ]

   
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20,help_text="your contact number")
    address = models.CharField(max_length=40, help_text="Enter your address Number")
    current_occupation = models.CharField(max_length=100)
    employer_name = models.CharField(max_length=100, blank=True)
    work_address = models.CharField(max_length=40,blank=True)
    work_contact_number = models.CharField(max_length=20, blank=True)
    educational_background = models.TextField()
    
    INTEREST_CHOICES = [
        ('Education', 'Education'),
        ('Healthcare', 'Healthcare'),
        ('Environment', 'Environment'),
        ('Human Rights', 'Human Rights'),
        ('Poverty Alleviation', 'Poverty Alleviation'),
        ('Community Development', 'Community Development'),
        ('Technology and innovation', 'Technology and innovation'),
        ('Leadership development', 'Leadership development'),
        ('Youth Empowerment', 'Youth Empowerment'),
        ('Others', 'Others'),
    ]

    nationality_choices = []
    with open('nationality.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            nationality_choices.append((row['Nationality'], row['Nationality']))
    

    language_choices = []
    with open('languages.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            language_choices.append((row['code'], row['name']))
    
    nationality = models.CharField(max_length=100, choices=nationality_choices ,help_text='which country are coming from ?')
    languages = models.CharField(max_length=100, choices=language_choices,help_text='The language Your Interested')
    areas_of_interest = models.CharField(max_length=100, choices=INTEREST_CHOICES,help_text='Area Your Interested in skills')
    volunteer_experience = models.TextField(blank=True,help_text='tell us your experience')
    reasons_for_joining = models.TextField(help_text='Reason why You want to join with this organization')
    availability_hours_per_week = models.TextField(help_text='Tell us the availability per Hour')
    availability_days = models.CharField(max_length=100,help_text='Show the availability')
    skills_qualifications = models.TextField(blank=True,help_text='Tell us Your Skills ')
    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_relationship = models.CharField(max_length=100)
    emergency_contact_number = models.CharField(max_length=20)
    medical_conditions = models.TextField(blank=True,help_text='any medical condition ? if yes Tell us about this condition')
    authorized_to_work = models.BooleanField( help_text="are you authorized to work ? if no Leave this field blank")
    criminal_convictions = models.BooleanField(help_text="ever you criminal participation ? if Yes Check this field otherwise leave blank")
    how_heard = models.CharField(max_length=255, blank=True)
    promise = models.BooleanField(default=False, help_text="Are you Agree Stay with us ? if No Leave this field blank")
