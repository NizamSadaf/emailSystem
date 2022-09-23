#from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import authenticate,login,logout
from registration.models import userData
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.core.mail import send_mail

# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username=request.POST.get("username")
            password=request.POST.get("password")
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('email_login')
            else :
                messages="Invalid Email or Password"
                return render(request,"login-form.html",{'messages':messages})
        return render(request,"login-form.html")

def log_out(request):
    logout(request)
    return redirect("index")



#def email_sendd(request):
    send_mail('hello', 'are halii', 'chompa1360@gmail.com',  ['smahi1314@gmail.com'], fail_silently=False, auth_user="chompa1360@gmail.com", auth_password='chompa117132', connection=None, html_message=None)
    return HttpResponse("SUCCES")