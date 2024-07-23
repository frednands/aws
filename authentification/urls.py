from django.urls import path
from . import  views

urlpatterns = [

    path('register/',views.register,name='register'),
    
     path('login/',views.login_view ,name='login'),
     
     path('dashboad/',views.dashboard ,name='dashboad'),
    
    path('login/save',views.login_user,name='login.store'),
    
    path('logout',views.user_logout,name='logout'),
    
    path('<str:token>/',views.activate_user),

    path('profile',views.editProfile,name='profile'),
    
    
    path('register/save',views.user_register,name='register.store')
]
