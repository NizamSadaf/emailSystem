
from datetime import datetime
from email import message
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
from outbox.models import sendData
import datetime
import random
global x,y,z
from .models import buffer
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def compose(request):
    if request.method == 'POST':
        recipient=request.POST.get('recipient_email')
        subject=request.POST.get('subject')
        messege=request.POST.get('messege')
        FROM = request.session.get('email_id')
        password=request.session.get('uid')
        try:
            send_mail(subject, messege,FROM,[recipient], fail_silently=False, auth_user=FROM, auth_password=password, connection=None, html_message=None)
            date=datetime.date.today()
            send_data=sendData(send_date=date,send_from=FROM,send_to=recipient,send_subject=subject,send_body=messege)
            send_data.save()
            talk("Messege Sent Successfully")
        except:
            return HttpResponse("Error Occured")
        return redirect('compose')
    
    else:
        return render(request,"compose.html")

def get_info():
    try:
        talk("speak after 1 seconds")
        r=sr.Recognizer()
        mic=sr.Microphone()
        with mic as source:
            audio = r.listen(source)
        text1=r.recognize_google(audio)
        #print(text)
        text=text1.lower()  
        return text
    except:
        return HttpResponse("Error Occured")
           
            #return render(request,'speak.html',{'msg':text})

def talk(text):
    engine=pyttsx3.init()
    engine.setProperty("rate", 178)
    engine.say(text)
    engine.runAndWait()



def get_email_info(request):
    try:
        if request.method == 'POST':
            talk('Please Give Recipient Email Address')
            email1=get_info()
            email2=email1.replace('at the rate of','@')
            email3=email2.replace('dot','.')
            email=email3.replace(' ','')
            talk('subject')
            subject=get_info()
            talk('messege')
            messege1=get_info()
            messege2=messege1.replace('full stop','.')
            messege3=messege2.replace('comma',',')
            messege4=messege3.replace('coma',',')
            messege5=messege4.replace('question mark','?')
            messege=messege5.replace('hyphen','-')
            my_dict={'email':email,'subject':subject,'messege':messege}
            encoded_string = urllib.parse.urlencode(my_dict)
            return redirect('compose/?%s'%encoded_string)

    except:
            return HttpResponse("Error Occured")  
        #return render(request,"compose.html")
          

def get_info():
    try:
        talk("speak after 1 seconds")
        r=sr.Recognizer()
        mic=sr.Microphone()
        with mic as source:
            audio = r.listen(source)
        text1=r.recognize_google(audio)
        #print(text)
        text=text1.lower()  
        return text
    except:
        return HttpResponse("Error Occured")
           
            #return render(request,'speak.html',{'msg':text})

def talk(text):
    engine=pyttsx3.init()
    engine.setProperty("rate", 178)
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        talk("speak after 1 seconds")
        r=sr.Recognizer()
        mic=sr.Microphone()
        with mic as source:
            audio = r.listen(source)
        text1=r.recognize_google(audio)
        #print(text)
        text=text1.lower()  
        return text
    except:
        return HttpResponse("Error Occured")

def recipient_email_id():
    try:
            talk('Please Give Recipient Email Address')
            email1=get_info()
            email2=email1.replace('at the rate of','@')
            email3=email2.replace('dot','.')
            email=email3.replace(' ','')
            return email
            
    except:
        return HttpResponse("Error Occured")
        
def email_subject():
    try:
            talk('subject')
            subject=get_info()
            return subject
    except:
        return HttpResponse("Error Occured")

def email_body():
    try:
            talk('messege')
            messege1=get_info()
            messege2=messege1.replace('full stop','.')
            messege3=messege2.replace('comma',',')
            messege4=messege3.replace('coma',',')
            messege5=messege4.replace('question mark','?')
            messege=messege5.replace('hyphen','-')
            return messege
    except:
        return HttpResponse("Error Occured")

def get_email_info(request):
    if request.method=="POST":
        uid=random.random()
        x = recipient_email_id()
        y= email_subject()
        z=email_body()
        buffer_data=buffer(uid=uid,email=x,sub=y,body=z)
        buffer_data.save()
        emails=buffer.objects.get(uid=uid)
        email=emails.email
        subject=emails.sub
        messege=emails.body
        id=emails.id
        # request.session['sub']=email_subject()
        # request.session['body']=email_body()
        # sub=request.session['sub']
        # body=request.session['body']
        return render(request,'get-email-info.html',{'email':email,'subject':subject,'messege':messege,'uid':id})
        #return render(request,"compose.html",{'email':email_id,'sub':sub,'body':body,'uid':id})
def get_email_info_compose(request):
    if request.method=="POST":
        recipient=request.POST.get('recipient_email')
        subject=request.POST.get('subject')
        messege=request.POST.get('messege')
        FROM = request.session.get('email_id')
        password=request.session.get('uid')
        try:
            send_mail(subject, messege,FROM,[recipient], fail_silently=False, auth_user=FROM, auth_password=password, connection=None, html_message=None)
            date=datetime.date.today()
            send_data=sendData(send_date=date,send_from=FROM,send_to=recipient,send_subject=subject,send_body=messege)
            send_data.save()
            talk("Messege Sent Successfully")
        except:
            return HttpResponse("Error Occured")
        return redirect('compose')
def edit(request):
    if request.method=="POST":
        talk("Wrong Messege")
        wrong=get_info()
        talk("correct messege")
        correct=get_info()
        uid=request.POST.get("uid")
        emails=buffer.objects.get(id=uid)
        x=emails.email
        y=emails.sub
        oldbody=emails.body
        newbody=oldbody.replace(wrong,correct)
        updatedemail=buffer(uid=uid,email=x,sub=y,body=newbody)
        updatedemail.save()
        emails1=buffer.objects.get(uid=uid)
        email=emails1.email
        subject=emails1.sub
        messege=emails1.body
        id=emails1.id
        return render(request,'edit.html',{'email':email,'subject':subject,'messege':messege,'uid':id})
        return render(request,"compose.html",{'email':email_id,'sub':sub,'body':body,'uid':id})
def edit_compose(request):
    if request.method=="POST":
        recipient=request.POST.get('recipient_email')
        subject=request.POST.get('subject')
        messege=request.POST.get('messege')
        FROM = request.session.get('email_id')
        password=request.session.get('uid')
        try:
            send_mail(subject, messege,FROM,[recipient], fail_silently=False, auth_user=FROM, auth_password=password, connection=None, html_message=None)
            date=datetime.date.today()
            send_data=sendData(send_date=date,send_from=FROM,send_to=recipient,send_subject=subject,send_body=messege)
            send_data.save()
            talk("Messege Sent Successfully")
        except:
            return HttpResponse("Error Occured")
        return redirect('compose')
def start(request):
    if request.method=="POST":
        talk("Start Messege")
        start_messege=email_body()
        uid=request.POST.get("uid")
        emails=buffer.objects.get(id=uid)
        x=emails.email
        y=emails.sub
        oldbody=emails.body
        newbody=oldbody+start_messege
        updatedemail=buffer(uid=uid,email=x,sub=y,body=newbody)
        updatedemail.save()
        emails1=buffer.objects.get(uid=uid)
        email=emails1.email
        subject=emails1.sub
        messege=emails1.body
        id=emails1.id
        return render(request,'start.html',{'email':email,'subject':subject,'messege':messege,'uid':id})
       # return render(request,"compose.html",{'email':email_id,'sub':sub,'body':body,'uid':id})
def start_compose(request):
    if request.method=="POST":
        recipient=request.POST.get('recipient_email')
        subject=request.POST.get('subject')
        messege=request.POST.get('messege')
        FROM = request.session.get('email_id')
        password=request.session.get('uid')
        try:
            send_mail(subject, messege,FROM,[recipient], fail_silently=False, auth_user=FROM, auth_password=password, connection=None, html_message=None)
            date=datetime.date.today()
            send_data=sendData(send_date=date,send_from=FROM,send_to=recipient,send_subject=subject,send_body=messege)
            send_data.save()
            talk("Messege Sent Successfully")
        except:
            return HttpResponse("Error Occured")
        return redirect('compose')     