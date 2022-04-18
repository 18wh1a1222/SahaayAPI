import email
from django.db import models

# Create your models here.

class Users(models.Model):
    aadharNo = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=50)
    phno = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=20)
    dob = models.DateField()
    type = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    email = models.EmailField(blank = True,unique=True)

class Needs(models.Model):
    needId = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    desc = models.CharField(max_length=300)
    pay = models.IntegerField()
    dop = models.DateField()
    doc = models.DateField(blank=True)
    status = models.CharField(max_length=10)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)

class Events(models.Model):
    eventId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    dop = models.DateField()
    doe = models.DateField()
    lastDay = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    
class Participants(models.Model):
    eventId = models.ForeignKey(Events, on_delete=models.CASCADE)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)

class TrackNeeds(models.Model):
    needId = models.ForeignKey(Needs, on_delete=models.CASCADE)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    paid = models.IntegerField()
    dop = models.DateField()
    desc = models.CharField(max_length=100, blank=True)

class Aadhar(models.Model):
    aadharId = models.CharField(max_length=12, unique=True)
    phno = models.CharField(max_length=10)
