from django.contrib import admin

from .models import Tutors, Endorsements

class TutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subjects', 'locations')
    list_display_links = ('id','name')
class EndorsementsAdmin(admin.ModelAdmin):
    list_display = ('target', 'endorsers')
admin.site.register(Tutors, TutorAdmin)
admin.site.register(Endorsements, EndorsementsAdmin)

