from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
    return render(request, 'pages/index.html')
# Create your views here.


def about(request):
    return render(request, 'pages/about.html')