import re
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import CreateProfileForm, UpdateProfileForm
from listings.models import Tutors, Endorsements
from django import forms
from contacts.models import Contact
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
def register(request):
    if request.method == 'POST':
    # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
        # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                # Looks good
                    user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')

@login_required
def dashboard(request):
  user_id = request.user.id
  try:
    tutor_profile = Tutors.objects.get(user_id = user_id)
  except:
    tutor_profile = None
  if tutor_profile:
    tutor_id = tutor_profile.id
    tutor_contacts = Contact.objects.order_by('-contact_date').filter(tutor_id = tutor_id)
    tasks = Task.objects.order_by('-submit_date').filter(is_published=True)
    context = {
      'contacts': tutor_contacts,
      'tasks': tasks,
    }
    return render(request, 'accounts/dashboard.html',context)
  if not tutor_profile:
    tasks = Task.objects.order_by('-submit_date').filter(is_published=True)
    context = {
      'tasks': tasks,
    }
    return render(request, 'accounts/start_dashboard.html', context)
# def create_profile(request):
#   try:
#     tutor = request.user.tutors
#     form = ProfileForm(instance=tutor)
#   except:
#     form = ProfileForm()
#   if request.method == 'POST':
#     form = ProfileForm(request.POST, request.FILES)
#     if form.is_valid():
#       print('form is valid')
#       form.save()


#   context = {'form':form}
#   return render(request, 'accounts/profile.html', context)

@login_required
def edit_profile(request):
  user_id = request.user.id
  try:
    profile = Tutors.objects.get(user_id = user_id )
  except:
    profile = None
  if profile:
    tutor = request.user.tutors
    tutor_id = request.user.id
    tutor_profile = Tutors.objects.get(user_id = tutor_id)
    form = UpdateProfileForm(instance= tutor)
    if request.method == 'POST':
      form = UpdateProfileForm(request.POST, request.FILES, instance = tutor_profile)
      if form.is_valid():
        form.save()
        print('wot')

    context = {'form':form, 'profile':profile}
    return render(request, 'accounts/profile.html', context)
  if not profile:
    tutor_id = request.user.id
    form = UpdateProfileForm()
    if request.method == 'POST':
      form = UpdateProfileForm(request.POST, request.FILES)
      if form.is_valid():
        tutor = form.save(commit=False)
        tutor.user_id = tutor_id  # The logged-in user
        tutor.save()
        print(tutor.user_id)
    context = {'form':form, 'profile':profile}
    return render(request, 'accounts/profile.html', context)
def endorse(request):
  tutor = request.user.tutors
  endorser_name = tutor.name
  if request.method == 'POST':
    target_name = request.POST['target']
    try:
      target_instance = Tutors.objects.get(name = target_name)
    except:
      target_instance = None
      messages.error(request, "No such tutor exists. Full name of tutor has to be exact.")
      return redirect('profile')
    if target_name == endorser_name:
      messages.error(request, "It doesn't make sense to self-endorse!")
      return redirect('profile')
    try:
      endorsement = Endorsements.objects.get(target = target_instance)
    except:
      endorsement = None
    if endorsement:
      if endorser_name in endorsement.endorsers:
        messages.error(request, "You have already endorsed this tutor")
        return redirect('profile')
      endorsement.endorsers.append(endorser_name)
      endorsement.save()
      messages.success(request, "Endorsement Successful")
    if not endorsement:
      endorsement_new = Endorsements.objects.create(target = target_instance, endorsers = [endorser_name])
      endorsement_new.save()
      messages.success(request, "Endorsement Successful")
  return redirect('profile')





  







  # try:
  #   tutor = request.user.tutors
  #   tutor_id = request.user.id
  #   tutor_profile = Tutors.objects.get(user_id = tutor_id)
  #   form = UpdateProfileForm(instance= tutor)
  #   if request.method == 'POST':
  #     form = UpdateProfileForm(request.POST, request.FILES, instance = tutor_profile)
  #     if form.is_valid():
  #       form.save()
        
  #   context = {'form':form}
  #   return render(request, 'accounts/profile.html', context)
  # except:
  #   tutor_id = request.user.id
  #   form = UpdateProfileForm()
  #   if request.method == 'POST':
  #     form = UpdateProfileForm(request.POST, request.FILES)
  #     if form.is_valid():
  #       form.save()
  #   context = {'form':form}
  #   return render(request, 'accounts/profile.html', context)