from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
 

    path("",views.home,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("patient",views.patient,name='patient'),
    path("doctor",views.doctor,name='doctor'),
    path("receptionist",views.receptionist,name='receptionist'),
    path("admin",views.admin,name='admin'),
    path("questionaries",views.questionaries,name='questionaries'),
    path('questionselect',views.questionselect,name='questionselect'),
    path('results',views.results,name='results'),


]