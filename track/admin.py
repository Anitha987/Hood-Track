from django.contrib import admin
from .models import Business,Neighbour,Profile
# Register your models here.
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Neighbour)