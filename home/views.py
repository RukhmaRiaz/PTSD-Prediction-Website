from urllib import response
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from home.models import Receptionist
from home.models import Patient
from home.models import Doctor
from home.models import Questionaries
from home.models import  Feedback
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
# Create your views here.
def home(request):
    #messages.success(request,"Query Sent Successfully")
    return render(request, 'home.html')
   # return HttpResponse( "this is homepage" )

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')


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
        name=request.POST.get('uname')
        email=request.POST.get('email')
        cnic=request.POST.get('cnic')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        contact=Contact(name=name,email=email,cnic=cnic,phone=phone, age=age, dob=dob, address=address, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Query has been Sent Successfully!')
    return render(request, 'receptionist.html')

def questionaries(request):
    return render(request, 'questionaries.html')

def questionselect(request):
    results=request.GET['option']
    return render(request, 'questionselect.html',{'option':results})

def LogoutPage(request):
    logout(request)
    return redirect('login')

def results(request):
    option=[]
    if request.method == 'POST':
        option = request.POST.getlist('option')
    return render(request, 'results.html',{'option':option})

def feedback(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        query=request.POST.get('query')
        contact=Contact(name=name,email=email,phone=phone,query=query,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Query has been Sent Successfully!')
    return render(request,'feedback.html')
