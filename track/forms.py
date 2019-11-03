from django import forms
from .models import Profile,Business,Neighbour

class ProfileForm(forms.ModelForm):
   class Meta:
        model = Profile
        exclude = ['']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }

class NeighbourForm(forms.ModelForm):
   class Meta:
        model = Neighbour
        exclude = ['']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }  

class BusinessForm(forms.ModelForm):
   class Meta:
        model = Business
        fields = ['image','name','email']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }
