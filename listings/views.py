from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Tutors
def index(request):
    tutors = Tutors.objects.all()
    paginator = Paginator(tutors,3)
    page = request.GET.get("page")
    paged_tutors = paginator.get_page(page)
    context = {
        'tutors':paged_tutors
    }
    return render(request, 'listings/listings.html',context)


def listing(request, tutor_id):
    tutors = get_object_or_404(Tutors, pk= tutor_id)
    context = {
        'tutors' : tutors
    }
    return render(request, 'listings/listing.html', context)
def search(request):
    return render(request, 'listings/search.html')


