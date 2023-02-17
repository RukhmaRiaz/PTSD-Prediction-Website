from django.db import models
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=11)
    query=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class Receptionist(models.Model):
    uname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    cnic=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    age=models.CharField(max_length=122)
    dob=models.CharField(max_length=122)
    address=models.CharField(max_length=122)
    date=models.DateField()
    def __str__(self):
        return self.uname

class Patient(models.Model):

    date=models.DateField()

    def __str__(self):
        return self.date

class Doctor(models.Model):

    date=models.DateField()

    def __str__(self):
        return self.date
    


class Questionaries(models.Model):
    date=models.DateField()
    def __str__(self):
       return self.date

class Result(models.Model):
    date=models.DateField()
    def __str__(self):
       return self.date
