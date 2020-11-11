from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super(City, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Profile(models.Model):
    current_city = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='images', blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.title