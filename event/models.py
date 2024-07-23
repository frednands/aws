from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length = 150,unique=True)
    image = models.ImageField(upload_to='event', height_field=None, width_field=None, max_length=100,default='/project/noimag.png')
    created_at = models.DateTimeField(auto_now=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)
    class Meta:
        
        managed = True
        verbose_name = 'event'
        verbose_name_plural = 'events'
        
    def __str__(self):
        return self.event_name

