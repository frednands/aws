from typing import Iterable
from .utils import Duration
from django.db import models
from PIL import Image

# Create your models here.

class Post(Duration):
    title = models.CharField(max_length = 150)
    description = models.TextField()
    is_publish = models.BooleanField(default=False)
    image = models.ImageField(upload_to="post",  max_length=100,null=False)
    
    def delete(self):
        self.image.delete()
        super().delete()
    
    def __str__(self):
        return self.title
    class Meta:
        managed = True
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ["-created_at"]
    
    
