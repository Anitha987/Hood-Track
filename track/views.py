from django.shortcuts import render
from .models import Business,Profile,Neighbour,User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def get_images(request):
    current_user = request.user
    images=Business.objects.all()
    return render(request,'my_track/index.html',{"images":images})

