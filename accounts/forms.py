from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from listings.models import Tutors, Endorsements

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Tutors
        fields = '__all__'
        exclude = ['user','list_date']
        labels = {
            'is_ars': 'ARS Certified',
            'is_published': 'Publish Profile',
            'education': 'Highest Education',
            'subjects': 'Subjects Tutoring',
            'levels': 'Levels Tutoring',
            'locations': 'Tutoring Locations',
            'photo_main': 'Main Photo (required)',
            'photo_1': 'Additional Photo (not required)',
            'photo_2': 'Additional Photo (not required)',
            'photo_3': 'Additional Photo (not required)',
            'photo_4': 'Additional Photo (not required)',
            'photo_5': 'Additional Photo (not required)',
            'photo_6': 'Additional Photo (not required)',
        }


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Tutors
        fields = '__all__'
        exclude = ['user','list_date']
        labels = {
            'is_ars': 'ARS Certified',
            'is_published': 'Publish Profile',
            'education': 'Highest Education',
            'subjects': 'Subjects Tutoring',
            'levels': 'Levels Tutoring',
            'locations': 'Tutoring Locations',
            'photo_main': 'Main Photo (required)',
            'photo_1': 'Additional Photo (not required)',
            'photo_2': 'Additional Photo (not required)',
            'photo_3': 'Additional Photo (not required)',
            'photo_4': 'Additional Photo (not required)',
            'photo_5': 'Additional Photo (not required)',
            'photo_6': 'Additional Photo (not required)',
        }
