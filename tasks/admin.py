from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
  list_display = ('id', 'subjects', 'level')
  list_display_links = ('id', 'subjects')
  list_per_page = 25

admin.site.register(Task, TaskAdmin)
