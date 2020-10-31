from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

#-----------STATIC PAGES
def home(request):
    return render(request, 'home.html')

#----------SIGNUP USER
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('new_profile')
        else: 
            error_message = 'Invalid sign up - try again'
            form = UserCreationForm()
            context = {'form': form, 'error_message': error_message}
            return render(request, 'registration/signup.html',context)
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

#---------------- PROFILE

@login_required
def new_profile(request):
    # profile = Profile.objects.get(id=user_id)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            new_profile = profile_form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            return redirect('user_profile', profile_id = new_profile.id)
        else :
            return render(request, 'profiles/detail.html', {'profile_form': profile_form})
    else: 
        form = ProfileForm()
        context = {'form': form}
        return render(request, 'profiles/new.html', context)

@login_required
def user_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profiles/detail.html', {'profile': profile})

