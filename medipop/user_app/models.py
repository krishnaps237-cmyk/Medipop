from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Register(AbstractUser):
    Address=models.CharField(max_length=200)
    Name=models.CharField(max_length=50)
    License_no=models.CharField(max_length=20)
    Phone_no=models.IntegerField(default=10)
    Approval_date=models.DateField(auto_now=True)
    Approval_status=models.CharField(max_length=200)
    Approval=models.BooleanField(default=True)
    usertype=models.CharField(choices=[('Admin','Admin'),('User','User'),('Pharmacist','Pharmacist')],max_length=10,default=True)