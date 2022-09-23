from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import authenticate,login,logout
from registration.models import userData
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.core.mail import send_mail

# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def email_login(request):
    if request.method == "POST":
        email_id=request.POST.get("email")
        uid=request.POST.get("uid")
        request.session['email_id']=email_id
        request.session['uid']=uid
        return redirect('home') 
    return render(request,"gmail_login.html")