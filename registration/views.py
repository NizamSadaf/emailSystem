from django.http import HttpResponse
from django.shortcuts import render,redirect
from registration.forms import Userdata
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password

def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if  request.method == 'POST':
        form=Userdata(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=Userdata()  
        
    return render(request,"registration-form.html",{'form':form})