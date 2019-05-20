from django import forms
from .models import Blog_post

class New_post (forms.ModelForm):
    class Meta:
        model = Blog_post
        fields = ['title', 'text']
