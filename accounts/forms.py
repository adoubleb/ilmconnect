from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from listings.models import Tutors

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Tutors
        fields = '__all__'
        exclude = ['list_date']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Tutors
        fields = '__all__'
        exclude = ['list_date']