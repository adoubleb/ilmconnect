from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<tutor_id>', views.listing, name = 'listing'),
    path('search', views.search, name = 'search')
]