from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from listings.models import Tutors
from listings.choices import location_choices, level_choices, subject_choices
def index(request):
    tutors = Tutors.objects.all()[:3]
    context = {
        'tutors': tutors,
        'location_choices': location_choices,
        'level_choices':level_choices,
        'subject_choices':subject_choices,
    }
    return render(request, 'pages/index.html', context)
# Create your views here.


def about(request):
    return render(request, 'pages/about.html')