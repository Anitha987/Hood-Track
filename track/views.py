from django.shortcuts import render,redirect
from .models import Business,Profile,Neighbour,User
from django.contrib.auth.decorators import login_required
from .forms import BusinessForm,ProfileForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def get_images(request):
    current_user = request.user
    images=Business.objects.all()
    return render(request,'my_track/index.html',{"images":images})

def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.Profile=profile
            image.save()
        return redirect('get')

    else:
        form = BusinessForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile=Profile.objects.filter(user=current_user).first()
    print(profile)
    images=Business.objects.filter(user=current_user)
    return render(request, 'my_track/new_profile.html', {"images":images,"profile":profile})
  
@login_required(login_url='/accounts/login/')
def profile_form(request):
   current_user = request.user
   if request.method == 'POST':
       form = ProfileForm(request.POST, request.FILES)
       if form.is_valid():
           profile = form.save(commit=False)
           profile.user = current_user
           profile.save()
       return redirect('profile')
   else:
       form = ProfileForm()
   return render(request, 'my_track/profileform.html', {"form": form})

@login_required(login_url='/accounts/login/')
def hood(request):
    current_user = request.user
    hood=Profile.objects.filter(user=current_user).first()
    print(profile)
    images=Business.objects.filter(user=current_user)
    return render(request, 'my_track/new_profile.html', {"images":images,"profile":profile})
  
@login_required(login_url='/accounts/login/')
def profile_form(request):
   current_user = request.user
   if request.method == 'POST':
       form = ProfileForm(request.POST, request.FILES)
       if form.is_valid():
           profile = form.save(commit=False)
           profile.user = current_user
           profile.save()
       return redirect('profile')
   else:
       form = ProfileForm()
   return render(request, 'my_track/profileform.html', {"form": form})

