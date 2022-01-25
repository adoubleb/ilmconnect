from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Tutors
from listings.choices import location_choices, level_choices, subject_choices
def index(request):
    tutors = Tutors.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(tutors,6)
    page = request.GET.get("page")
    paged_tutors = paginator.get_page(page)
    context = {
        'tutors':paged_tutors
    }
    return render(request, 'listings/listings.html',context)


def listing(request, tutor_id):
    tutors = get_object_or_404(Tutors, pk=tutor_id)
    context = {
        'tutors': tutors
    }
    return render(request, 'listings/listing.html', context)
    
def search(request):
    queryset_list = Tutors.objects.all()
    if 'subject' in request.GET:
        subject = request.GET['subject']
        if subject:
            queryset_list = queryset_list.filter(subjects__contains=subject)
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            queryset_list = queryset_list.filter(locations__contains=location)
    if 'level' in request.GET:
        level = request.GET['level']
        if level:
            queryset_list = queryset_list.filter(levels__contains=level)
    if 'ARS-Certified' in request.GET:
        is_Ars = request.GET['ARS-Certified']
        if is_Ars:
            queryset_list = queryset_list.filter(is_ars=True)
    queryset_list = queryset_list.filter(is_published=True)
        
    context = {
        'tutors': queryset_list,
        'location_choices': location_choices,
        'level_choices':level_choices,
        'subject_choices':subject_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)


