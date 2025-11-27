from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        username=request.POST.get("Username")
        email=request.POST.get("email")
        phone_no=request.POST.get("phone")
        license_no=request.POST.get("license")
        Address=request.POST.get("Address")
        password=request.POST.get("pwd")
       
       
        if Register.objects.filter(username=username).exists():
          messages.error(request,"username already exists")
        if Register.objects.filter(email=email).exists():
          messages.error(request,"email already exists")
        Register.objects.create(username=username,email=email,Phone_no=phone_no,License_no=license_no,Address=Address,password=password,Approval_status="Approved",usertype="User")
        messages.success(request,"Registration successful")
        return redirect('login')
    return render (request,'register.html')  
      

def login_user(request):
    if request.method=="POST":
         username=request.POST.get("Username")
         password=request.POST.get("pwd")
         user=authentication(request,username=username,password=password)
         if user:
            login(request,user)
            messages.success(request,'login success')
            return redirect('index')
        else: 
            messages.error(request,'login failed,invalid username or password')
    return render(request,'login.html')