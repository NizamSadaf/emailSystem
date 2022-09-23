from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import authenticate,login,logout
from registration.models import userData
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.core.mail import send_mail
import speech_recognition as sr
import pyttsx3
import urllib.parse
import imaplib
from django.core.paginator import Paginator
from outbox.models import sendData
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def outbox(request):
    email_id=request.session.get('email_id')
    emails=sendData.objects.filter(send_from=email_id).order_by('id').reverse()
    p=Paginator(emails,5)
    page_number=request.GET.get('page')
    emails =p.get_page(page_number)
    return render(request,"outbox.html",{'emails':emails})

def showw(request,sub):
    email_data=sendData.objects.get(send_subject=sub)
    return render(request,"outbox_message.html",{'message':email_data})

def speakk(request,sub):
    email_data=sendData.objects.get(send_subject=sub)
    talkk("Receiver Email Address is")
    talkk(email_data.send_to)
    talkk("Message is")
    talkk(email_data.send_body)
    return redirect('outbox')

def talkk(email_data):
    engine=pyttsx3.init()
    engine.setProperty("rate", 178)
    engine.say(email_data)
    engine.runAndWait()

def deletee(request,sub):
    instance = sendData.objects.get(send_subject=sub)
    instance.delete()
    return redirect('outbox')

def outbox_search(request):
    sub=request.POST.get('subject')
    username=request.session.get('email_id')
    #emails=emailData.objects.filter(email_to=username)
    emails=sendData.objects.filter(send_subject__contains=sub,send_from=username).order_by('id').reverse()
    return render(request,"outbox.html",{'emails':emails})