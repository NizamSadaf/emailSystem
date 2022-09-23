from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import authenticate,login,logout
from registration.models import userData
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.core.mail import send_mail
import speech_recognition as sr
import pyttsx3
# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def home(request):
        email_id=request.session.get('email_id')
        password=request.session.get('password')
        option=choose()
        if(option=='manual'):
            return render(request,"home.html",{'user':request.user,'email_id':email_id,'password':password})
        else:    
            try:
                name=get_menu_info()
                menu=name.replace(" ","")
                return redirect(menu)
            except:
                talk("I cannot hear")
                return redirect("home")
        context={'user':'request.user','email_id':email_id,'password':password}
        #return render(request,"home.html",{'user':request.user,'email_id':email_id,'password':password})


def choose():
    talk("What you want Manual or Automated")
    text=get_info()
    return text    
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
def get_menu_info():
         talk("Welcome to Home page where do you want to go compose,inbox,outbox,logout")
         item=get_info()
         return item

def index(request):
    return render(request,"index.html")