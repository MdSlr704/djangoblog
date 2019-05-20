from django.shortcuts import render ,redirect, get_object_or_404
from .models import Blog_post
from .forms import New_post

def homepage (request):
    qs = Blog_post.objects.all()
    return render (request,'bloghomepage.html',{'posts' : qs})
def new_post (request):
    if not request.user.is_authenticated:
        return render(request, 'registration/loginfirst.html',{})
    if request.method == 'POST':
        form = New_post(request.POST)
        if form.is_valid:
            form.save()
            return redirect('http://127.0.0.1:8000/blog/')
    else:
        form = New_post()
    return render(request,'newpost.html',{'form':form})
def edit_post (request,id):
    obj = get_object_or_404(Blog_post,id = id)
    if not request.user.is_authenticated:
        return render(request, 'registration/loginfirst.html',{})
    if request.method == 'POST':
        form = New_post(request.POST, instance = obj)
        if form.is_valid:
            form.save()
            return redirect('http://127.0.0.1:8000/blog/')
    else:
        form = New_post(instance = obj)
    return render(request, 'newpost.html',{'form':form})
def delete_post (request,id):
    if not request.user.is_authenticated:
        return render(request, 'registration/loginfirst.html',{})
    if request.method == 'POST':
        obj = get_object_or_404(Blog_post, id = id )
        obj.delete()
        return redirect('http://127.0.0.1:8000/blog/')
    else:
        return render(request,'deletepost.html',{})
