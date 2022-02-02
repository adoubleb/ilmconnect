import re
from django.shortcuts import render, redirect
from .models import Task
from django.contrib import messages

def submit_task(request):
  if request.method == 'POST':
    phone = request.POST['phone']
    email = request.POST['email']
    subject = request.POST['subject']
    level = request.POST['level']
    location = request.POST['location']
    rate = request.POST['rate']
    message = request.POST['message']

    #  Check if user has made inquiry already

    task = Task(phone=phone, email=email, subjects=subject, level=level, locations=location, rate=rate, description=message )

    task.save()

    # Send email
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #   'traversy.brad@gmail.com',
    #   [realtor_email, 'techguyinfo@gmail.com'],
    #   fail_silently=False
    # # )
    

    messages.success(request, 'Your task has been submitted, details will be made accessible to registered tutors.')

    return redirect('/tasks/display_task')

def display_task(request):
    return render(request, 'tasks/submit_task.html')
def delete_task(request):
  if request.method == 'POST':
    phone = request.POST['phone']
    email = request.POST['email']
    target = Task.objects.all().filter(phone = phone, email = email)
    if target:
      for t in target:
        t.delete()
      messages.success(request, 'Your tasks has been deleted.')
    else:
      messages.error(request,'No such tasks, double check input phone number and email.')
    return redirect('/tasks/display_task')

