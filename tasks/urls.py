from django.urls import path

from . import views

urlpatterns = [
  path('submit_task', views.submit_task, name='submit_task'),
  path('display_task',views.display_task, name='display_task')
]