from email import message
from django.db.models.query import InstanceCheckMeta
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.decorators import login_required, login_required
from django.views.decorators.cache import cache_control
import imaplib
import email 
import pyttsx3
from inbox.models import emailData
from django.core.paginator import Paginator
from ast import literal_eval
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def inbox(request):
    id=0
    email_msg={}
    my_msg_body=[]
    username=request.session.get('email_id')
    password=request.session.get('uid')
    # mail = imaplib.IMAP4('127.0.0.1',143)
    # mail.login(username, password)
    mail = imaplib.IMAP4_SSL('imap.mail.yahoo.com')
    mail.login(username, password)
    mail.select('Inbox')  # refresh inbox
    status, message_ids = mail.search(None, 'UNSEEN')  # get all emails
    for message_id in message_ids[0].split():  # returns all message ids
    # for every id get the actual email
        id=id+1
        status, message_data = mail.fetch(message_id, '(RFC822)')
        actual_message = email.message_from_bytes(message_data[0][1])
        
        
        for part in actual_message.walk():
            if part.get_content_type() == 'text/plain':
                body1=part.get_payload(decode=True)
                
                body=body1.decode()
                email_date = actual_message["Date"]
                subject = actual_message["Subject"]
                sender=actual_message["From"]
                to=actual_message["To"]
                #email_msg={'id':id,'date':email_date,'sub':subject,'body':body}
                email_data=emailData(email_date=email_date,email_from=sender,email_to=to,email_subject=subject,email_body=body)
                email_data.save()
                
    email_id=request.session.get('email_id')
    emails=emailData.objects.filter(email_to=email_id).order_by('id')[::-1]
    p=Paginator(emails,5)
    page_number=request.GET.get('page')
    emails =p.get_page(page_number)
    return render(request,"show.html",{'emails':emails})
       # return HttpResponse(subject)


def show(request,sub):
    email_data=emailData.objects.get(email_subject=sub)
    
    return render(request,"message.html",{'message':email_data})
    

def speak(request,sub):
    email_data=emailData.objects.get(email_subject=sub)
    talk("Sender Email Address is")
    talk(email_data.email_from)
    talk("Message is")
    talk(email_data.email_body)
    return redirect('inbox')
def talk(email_data):
    engine=pyttsx3.init()
    engine.setProperty("rate", 178)
    engine.say(email_data)
    engine.runAndWait()

def delete(request,sub):
    instance = emailData.objects.get(email_subject=sub)
    instance.delete()
    return redirect('inbox')

def search(request):
    sub=request.POST.get('subject')
    username=request.session.get('email_id')
    
    emails=emailData.objects.filter(email_subject__contains=sub,email_to=username).order_by('id')[::-1]
    return render(request,"show.html",{'emails':emails})