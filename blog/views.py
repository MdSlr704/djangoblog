from django.shortcuts import render
from .models import Blog_post

def homepage (request):
    qs = Blog_post.objects.all()
    return render (request,'bloghomepage.html',{'posts' : qs})
