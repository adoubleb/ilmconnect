from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    tutor_id = request.POST['tutor_id']
    tutor = request.POST['tutor']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    subject = request.POST['subject']
    level = request.POST['level']
    location = request.POST['location']
    message = request.POST['message']
    tutor_email = request.POST['tutor_email']


    contact = Contact(tutor=tutor, tutor_id=tutor_id, name=name, phone=phone, message=message, subject=subject, level=level, location=location, email=email)
    contact.save()

    # Send email
    send_mail(
      'ILMC Tutor Inquiry',
      f"There has been an inquiry for {tutor}. Name of inquirer: {name}. Subject of inquiry: {subject}. Level of inquiry: {level}. Location: {location} . Phone number of tutee:  {phone}. Email of tutee: {email}.  Additional message by tutee:  {message}.",
      'ilmconnecttechguy@gmail.com',
      [tutor_email, 'blowurmind007@gmail.com'],
      fail_silently=False
    )

    messages.success(request, 'Your request has been submitted, the tutor will get back to you soon')
    return redirect('/listings/'+tutor_id)
