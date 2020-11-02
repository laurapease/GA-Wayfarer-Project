from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Profile(models.Model):
    current_city = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='images')
    join_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.current_city

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.title