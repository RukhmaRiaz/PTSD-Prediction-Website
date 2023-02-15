"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views


admin.site.site_header = "PTSD Predictor Admin"
admin.site.site_title = "PTSD Admin Portal"
admin.site.index_title = "Welcome to our PTSD Detection System "

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('/patient',views.patient, name= 'patient'),
    path('/patient/login/',views.LoginPage, name= 'login'),
    path('/doctor',views.doctor, name= 'doctor' ),
    path('/doctor/login/', views.Logindoctor, name= 'logindoctor'),
    path('/doctor/login/questionaries', views.questionaries, name= 'questionaries'),

    ]
