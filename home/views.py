from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context={
        "variable1":"Sent",
        "variable2":"Rukhma is Girl"
    }
    return render(request, 'index.html', context)
   # return HttpResponse( "this is homepage" )

def about(request):
    return render(request, 'about.html')
    #return HttpResponse( "this is about page" )

def services(request):
    return render(request, 'services.html')
    #return HttpResponse( "this is services page" )

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse( "this is contact page" )

def patient(request):
    return render(request, 'patient.html')
    #return HttpResponse( "this is patient page" )

def doctor(request):
    return render(request, 'doctor.html')
    #return HttpResponse( "this is doctor page" )

def admin(request):
    return render(request, 'admin.html')
    #return HttpResponse( "this is admin page" )

def receptionist(request):
    return render(request, 'receptionist.html')
    #return HttpResponse( "this is receptionist page" )