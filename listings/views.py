from django.shortcuts import render

from .models import Tutors
def index(request):
    tutors = Tutors.objects.all()
    context = {
        'tutors':tutors
    }
    return render(request, 'listings/listings.html',context)

def listing(request):
    return render(request, 'listing/listings.html')

def search(request):
    return render(request, 'listings/search.html')


