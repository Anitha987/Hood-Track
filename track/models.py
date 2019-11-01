from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Neighbour(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    occupant= models.CharField(max_length=30)


class Business(models.Models):
    image=models.ImageField(upload_to ='pictures')
    name = models.CharField(max_length=30)
    neighbour = models.ForeignKey(user)
    email=models.CharField(max_length=30)

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'photos',null=True,blank=True)
    location = models.TextField(max_length=60)


         

