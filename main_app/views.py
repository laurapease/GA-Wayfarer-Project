from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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

def new_profile(request, user_id):
    profile = Profile.objects.get(id=user_id)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            new_profile = profile_form.save(commit=False)
            new_profie.user = request.user
            new_profile.save()
            return redirect('user_profile', new_profile.id)
    else: 
        form = ProfileForm()
        context = {'form': form}
        return render(request, 'profiles/new.html', context)

def user_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profiles/show.html', {'profile': profile})

