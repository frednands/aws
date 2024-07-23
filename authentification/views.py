from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from validate_email import validate_email
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.conf import settings
from helpers.decorators import auth_user_should_not_access
from django.contrib.sites.shortcuts import get_current_site
import random
import threading
import csv
from django.shortcuts import render
from django.conf import settings
import os

# Create your views here

from django.contrib.auth.decorators import login_required



class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()
  



@auth_user_should_not_access
def register(request):
    return render(request,'auth/register.html')

@auth_user_should_not_access
@csrf_exempt
def user_register(request):
    
    if request.method == "POST":
        
        username = request.POST['user_name']
        
        first_name = request.POST['first_name']
        
        last_name = request.POST['last_name']
        
        email = request.POST['email']
        
        password = request.POST['password']
        
        password2 = request.POST['password2']
        
        context={'has_err':False}
        
        if  len(password) < 4 :
            
            messages.add_message(request,messages.ERROR,'password require atleast 4 characters')
            
            context['has_err'] = True
       
        if password != password2:
            
            messages.add_message(request,messages.ERROR,'your password does not match ')
            
            context['has_err'] = True 
        
        if not validate_email(email):
            
            context['has_err'] = True
            
            messages.add_message(request,messages.ERROR,'your email is invalid ')
          
        if User.objects.filter(username=username).exists():
                messages.add_message(request,messages.ERROR,'your username exist try another  ')
                context['has_err'] = True 
         
        if User.objects.filter(email=email).exists():
            
                messages.add_message(request,messages.ERROR,'your email exists  try another  ')
                
                context['has_err'] = True 
        
        if  context['has_err']:
            return render(request,'auth/register.html',{'data':request.POST})
        
        token =str(random.random()).split('.')[1]
        user = User.objects.create_user(username=username,email=email ,password=password,first_name=first_name,last_name=last_name)
        user.is_active = True
        user.is_email_verified = True
        user.set_password(password)
        user.token=token
        # domain = get_current_site(request).domain
        # link = f"http://{domain}/verify/{token}" or f"https://{domain}/verify/{token}"
        # email_subject ="Email Verification"
        # email_body=f"Hi {user.username} thank you for joining  us,click here {link}  to verify your account "
        
        # email = EmailMessage(subject=email_subject, body=email_body,
        #                  from_email=settings.EMAIL_FROM_USER,
        #                  to=[user.email]
        #                  )
        # EmailThread(email).start()

        
        user.save()
        messages.add_message(request, messages.SUCCESS,
                                 'Congratulations you have successfully join to Tayco organization.')
        return redirect('login')
        
    return render(request,'auth/login.html')



@auth_user_should_not_access
def login_view(request):
    return render(request,'auth/login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,'Your now logout ')
    return redirect(reverse('login'))

@login_required
def dashboard(request):
    return render(request,'member/dashboad.html')

@auth_user_should_not_access
def login_user(request):

    if request.method == 'POST':
        context = {'data': request.POST}
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user and not user.is_email_verified:
            context['err'] = True
            messages.add_message(request, messages.ERROR,
                                 'Email is not verified, please check your email inbox')
            return render(request, 'auth/login.html', context, status=401)

        if not user:
            messages.add_message(request, messages.ERROR,
                                 'Invalid credentials, try again')
            return render(request, 'auth/login.html', context, status=401)

        login(request, user)
        if not request.user.is_staff:
            messages.add_message(request, messages.SUCCESS,
                             f'Welcome {user.username}')

            return redirect(reverse('dashboad'))
        return redirect('/admin')

        

    return render(request, 'auth/login.html')


   

   

def activate_user(request, token):

    try:

        user = User.objects.filter(token=token).get()
        print(user)
    except Exception as e:
        user = None

    if user  :
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             'Email verified, you can now login')
        return redirect(reverse('login'))
    messages.add_message(request, messages.ERROR,
                                 'Invalid Token, try again')
    return render(request, 'auth/login.html',  status=401)

# @login_required
# @login_required
def editProfile(request):
    csv_file_path = os.path.join(settings.BASE_DIR, 'nationality.csv')  # Path to your CSV file

    data = []
    with open(csv_file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)  # Assuming the first row contains headers
        for row in csvreader:
            data.append(row)
    options = []
    if data:
        options = [row[0] for row in data]
    print(options);

    context ={
           'options': options,
       }
    return render(request, 'profile/profile.html',context)

# @login_required

