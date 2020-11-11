from django import forms
from .models import *

class ProfileForm(forms.ModelForm):

    class Meta: 
        model = Profile
        fields = ['current_city', 'avatar']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post 
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['title', 'content']