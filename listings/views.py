from django.shortcuts import render

def index(request):
    return render(request, 'listings/listings.html')

def listing(request):
    return render(request, 'listing/listings.html')

def search(request):
    return render(request, 'search/listings.html')


