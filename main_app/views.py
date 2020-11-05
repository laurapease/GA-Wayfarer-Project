from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from .models import Profile, Post, City
from .forms import ProfileForm, PostForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

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
            error_message = 'Username is already in use. Please enter another name.'
            form = UserCreationForm()
            context = {'form': form, 'error_message': error_message}
            return render(request, 'registration/signup.html',context)
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

#---------------- PROFILE

@login_required
def new_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            
            return redirect('user_profile', new_profile.id)
        else:
            return render(request, 'profile/new.html', {'form': form})
    else: 
        form = ProfileForm()
        context = {'form': form}
        return render(request, 'profile/new.html', context)

@login_required
def user_profile(request, profile_id):
    profile = Profile.objects.get(user = request.user)
    return render(request, 'profile/index.html', {'profile': profile})

@login_required
def profile(request):#also known as profile index
    print(request.user)
    profile = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(user = request.user)
    
    context = {'profile': profile, 'posts':posts}
    return render(request,'profile/index.html', context)

@login_required
def edit_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    if request.user == profile.user:
        if request.method == 'POST':
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
            if profile_form.is_valid():
                updated_profile = profile_form.save()
                return redirect('profile')
        else:
            form = ProfileForm(instance=profile)
            context = {'form': form}
            return render(request, 'profile/edit.html', context)
    
    else: 
        raise PermissionDenied("You are not authorized to edit")

#----------------POSTS

@login_required
def view_post(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {'post': post}
    return render(request, 'post/show.html', context)

@login_required
def add_post(request, city_id):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.city_id = city_id
            new_post.save()
            return redirect('view_city', city_id)
    else: 
        form = PostForm()
        context = {'form': form, 'city_id': city_id}
        return render(request, 'post/new.html', context)

@login_required
def delete_post(request, city_id, post_id):
    post = Post.objects.get(id=post_id)

    if request.user == post.user:
        post.delete()
    
        return redirect('view_city', city_id=city_id)

    else: 
        raise PermissionDenied("You are not authorized to delete")

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)    

    if request.user == post.user:

        if request.method == 'POST':
            post_form = PostForm(request.POST, instance=post)
            if post_form.is_valid():
                updated_post = post_form.save()
                return redirect('view_post', updated_post.id)

        else: 
            form = PostForm(instance=post)
            context = {'form': form}
            return render(request, 'post/edit.html', context)

    else: 
        raise PermissionDenied("You are not authorized to edit")


#---------------- CITIES

@login_required
def cities_index(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request, 'city/index.html', context)

@login_required
def view_city(request, slug):

    city = City.objects.get(slug=slug)
    posts = Post.objects.filter(city=city).order_by('-timestamp')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    context = {'city': city, 'posts': posts}
    return render(request, 'city/show.html', context)