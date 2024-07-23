from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User  # Import User model
    # models.py


class User(AbstractUser):
    token = models.CharField(max_length = 150)
    is_email_verified = models.BooleanField(default=False)
    
    profile = models.ImageField(upload_to="profile", height_field=None, width_field=None, max_length=100,default='profile/avatar.jpg')
    
    def __str__(self):
        return self.first_name+ ' '+ self.last_name

class Position(models.Model):
    position_name = models.CharField(max_length = 150)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)
    image = models.ImageField(upload_to='position',height_field=None, width_field=None, max_length=100,default='/position/default.jpg')
        
    
    class Meta:
        
        managed = True
        verbose_name = 'position'
        verbose_name_plural = 'positions'
        
    def __str__(self):
        return self.position_name

    

