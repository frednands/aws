# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Questions

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = [
            'gender', 'date_of_birth', 'nationality', 'contact_number', 'address',
            'current_occupation', 'employer_name', 'work_address', 'work_contact_number',
            'educational_background', 'areas_of_interest', 'volunteer_experience',
            'reasons_for_joining', 'availability_hours_per_week', 'availability_days',
            'skills_qualifications', 'languages', 'emergency_contact_name', 
            'emergency_contact_relationship', 'emergency_contact_number', 'medical_conditions',
            'authorized_to_work', 'criminal_convictions', 'how_heard', 'promise'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'availability_days': forms.CheckboxSelectMultiple(choices=[
                ('Monday', 'Monday'),
                ('Tuesday', 'Tuesday'),
                ('Wednesday', 'Wednesday'),
                ('Thursday', 'Thursday'),
                ('Friday', 'Friday'),
                ('Saturday', 'Saturday'),
                ('Sunday', 'Sunday'),
            ]),
            'areas_of_interest': forms.CheckboxSelectMultiple(),
        }
