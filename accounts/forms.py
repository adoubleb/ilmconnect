from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from listings.models import Tutors

class ProfileForm(forms.ModelForm):
  
    class Meta:
        model = Tutors
        fields = '__all__'
        exclude = ['user', 'list_date']