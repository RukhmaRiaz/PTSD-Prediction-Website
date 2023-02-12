from django.contrib import admin
from home.models import Contact
from home.models import Receptionist
from home.models import Patient
from home.models import Doctor
from home.models import Signup
from home.models import Login


# Register your models here.
admin.site.register(Login)
admin.site.register(Contact)
admin.site.register(Receptionist)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Signup)