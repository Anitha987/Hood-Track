from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Neighbour(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    occupant= models.CharField(max_length=30)

  def __str__(self):
      return self.name

class Business(models.Models):
    name = models.CharField(max_length=30)
    neighbour = models.ForeignKey(user)

