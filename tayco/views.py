from django.shortcuts import render
from project.models import Project
from client.models import Client
from authentification.models import Position
from event.models import Event
from post.models import Post
import csv

def index(request):
    
    projects = Project.objects.all().order_by('-created_at')[0:5]
    posts = Post.objects.all().order_by('-created_at')[:6]
    positions=Position.objects.all().order_by('-created_at')[:6]
    events=Event.objects.all().order_by('-created_at')[:4]
    clients = Client.objects.all()
    context = {
        'positions':positions,
        'clients':clients,
        'projects':projects,
        'events':events,
        'posts':posts,

   
    }
   
    return render(request,'index.html',context)



def about(request):
    return render(request,'about_us.html')

def contact(request):
    return render(request,'contact.html')