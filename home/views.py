from urllib import response
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate
from home.models import Receptionist
from home.models import Patient
from home.models import Doctor
from home.models import Questionaries




# Create your views here.
def index(request):
    #messages.success(request,"Query Sent Successfully")
    return render(request, 'index.html')
   # return HttpResponse( "this is homepage" )



def about(request):
    return render(request, 'about.html')
    #return HttpResponse( "this is about page" )

def services(request):
    return render(request, 'services.html')
    #return HttpResponse( "this is services page" )

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        query=request.POST.get('query')
        contact=Contact(name=name,email=email,phone=phone,query=query,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Query has been Sent Successfully!')
    return render(request, 'contact.html')
    #return HttpResponse( "this is contact page" )

def patient(request):          
    return render (request,'patient.html')
    #return HttpResponse( "this is patient page" )



def doctor(request):
          
    return render (request,'doctor.html')
    #return HttpResponse( "this is doctor page" )

def admin(request):
    return render(request, 'admin.html')
    #return HttpResponse( "this is admin page" )

def receptionist(request):
    if request.method=="POST":
        uname=request.POST.get('uname'),
        email=request.POST.get('email'),
        cnic=request.POST.get('cnic'),
        phone=request.POST.get('phone'),
        age=request.POST.get('age'),
        dob=request.POST.get('dob'),
        address=request.POST.get('address')

        receptionist=Receptionist(uname=uname,email=email,cnic=cnic,phone=phone,age=age,dob=dob,address=address,date=datetime.today())
        receptionist.save()
        messages.success(request, 'Receptionist Created Successfully!')
    return render(request, 'receptionist.html')
    #return HttpResponse( "this is receptionist page" )


def questionaries(request):
    return render(request, 'questionaries.html')

def questionselect(request):
    results=request.GET['option']
    return render(request, 'questionselect.html',{'option':results})
