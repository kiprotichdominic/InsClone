from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    caption = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images/')
    bio = models.CharField(max_length=180)