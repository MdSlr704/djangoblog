from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

def homepage (request):
    return render(request,'homepage.html',{})
def signup (request):
    if request.method == 'POST':
        print('request got')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print ('form is valid')
            form.save()
            return redirect('http://127.0.0.1:8000/accounts/login/')
    else :
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})
def logout (request):
    if not request.user.is_authenticated:
        return render(request, 'registration/loginfirst.html',{})
    return render(request,'registration/logout.html')
