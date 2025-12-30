from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

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
        name=request.POST.get("name")
       
       
        if Register.objects.filter(username=username).exists():
          messages.error(request,"username already exists")
        if Register.objects.filter(email=email).exists():
          messages.error(request,"email already exists")
        Register.objects.create_user(username=username,email=email,Phone_no=phone_no,License_no=license_no,Address=Address,password=password,Approval_status="Approved",usertype="User",Name=name)
        messages.success(request,"Registration successful")
        return redirect('login')
    return render (request,'register.html')  
      

def login_user(request):
    if request.method=="POST":
        username=request.POST.get("Username")
        password=request.POST.get("pwd")
        user=authenticate(request,username=username,password=password)
        if user:
            if not user.is_active:
                messages.error(request,'Your account is deactivated')
                return redirect('login')
            login(request,user)
            messages.success(request,'login success')
            return redirect('index')
        else: 
            messages.error(request,'login failed,invalid username or password or account deactivated')
    return render(request,'login.html')
def logout_user(request):
    logout(request)
    return redirect('index')
def views_user(request):
    users=Register.objects.filter(is_superuser=False)
    return render(request,'view_user.html',{'users':users})
def deactivate_user(request,id):
    user=Register.objects.get(id=id)
    user.is_active=False
    user.save()
    return redirect('view_user')
def activate_user(request,id):
    user=Register.objects.get(id=id)
    user.is_active=True
    user.save()
    return redirect('view_user')
def profile(request):
    user=request.user
    return render(request,'profile.html',{'user': user})
def edit_profile(request):
    user=request.user
    if request.method=="POST":
        name=request.POST.get("name")
        phone_no=request.POST.get("phone")
        license_no=request.POST.get("license")
        Address=request.POST.get("Address")
        username=request.POST.get("Username")
        email=request.POST.get("email")
        if Register.objects.filter(username=username).exclude(id=request.user.id).exists():
          messages.error(request,"username already exists")
        if Register.objects.filter(email=email).exclude(id=request.user.id).exists():
          messages.error(request,"email already exists")
        user.email=email
        user.Name=name
        user.Phone_no=phone_no
        user.License_no=license_no      
        user.Address=Address
        user.username=username
        user.save()
        messages.success(request,"Profile updated successfully")
        return redirect('profile')
    else:
        user=request.user
        return render(request,'edit_profile.html',{'user':user})
