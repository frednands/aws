from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.register, name='profile_detail'),
  
]
