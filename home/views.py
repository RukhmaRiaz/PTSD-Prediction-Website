from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from home.models import Receptionist
from home.models import Patient
from home.models import Doctor
from home.models import Signup
from home.models import Login
from home.models import Questionaries

# Create your views here.
def index(request):
    context={
        "variable1":"Sent",
        "variable2":"Rukhma is Girl"
    }
    #messages.success(request,"Query Sent Successfully")
    return render(request, 'index.html', context)
   # return HttpResponse( "this is homepage" )


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password doesn't match!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return render(request, 'login.html')
        
          
    return render (request,'signupl.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return render (request,'index.html')
        else:
            return HttpResponse("Username or Password is incorrect!")

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
    if request.method=="POST":
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        patient=Patient(uname=uname,password=password,date=datetime.today())
        patient.save()
        messages.success(request, 'Login Successfully!')
    return render(request, 'patient.html')
    #return HttpResponse( "this is patient page" )

def doctor(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        doctor=Doctor(uname=uname,password=password,date=datetime.today())
        doctor.save()
        messages.success(request, 'Login Successfully!')
    return render(request, 'doctor.html')
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



def signup(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        rpassword=request.POST.get('rpassword')
        signup=Signup(uname=uname,email=email,password=password,rpassword=rpassword,date=datetime.today())
        signup.save()
        messages.success(request, 'Signup Successfully!')
    return render(request,'signup.html','patient.html')

<<<<<<< HEAD
=======
def logout(request):
    logout(request)
    return redirect("/login")
def questionaries(request):
    return render(request, 'questionaries.html')
>>>>>>> b3ccc898c52b5f71e1bce26805abb335c67460fc
