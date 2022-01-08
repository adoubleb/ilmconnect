from django.contrib import admin

from .models import Tutors

class TutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subjects', 'locations')
    list_display_links = ('id','name')
admin.site.register(Tutors, TutorAdmin)
