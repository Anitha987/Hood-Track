from django.shortcuts import render
from .models import Business,Profile,Neighbour,User

# Create your views here.
def get_images(request):
    current_user = request.user
    images=Project.objects.all()
    return render(request,'my_awards/index.html',{"images":images})

