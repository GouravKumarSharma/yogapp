from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import Instructor
# Create your views here.
def loginpage(request):
    return render(request,'loginapp.html')
def register(request):
    if request.method=='POST':
        user = ""
        name=request.POST['name']
        fathers_name=request.POST['fname']
        aadhar=request.POST['aadhar']
        address=request.POST['address']
        experiance=request.POST['experiance']
        city=request.POST['city']
        resume=request.POST['resume']
        profile=request.POST['profile']
        email=request.POST['email']
        dob=request.POST['dob']
        mobile=request.POST['mobile']
        qualification=request.POST['qualification']
        joblocation=request.POST['jobloc']
        pic1=request.POST['pic1']
        pic2=request.POST['pic2']
        pic3=request.POST['pic3']
        pic4=request.POST['pic4']
        password=request.POST['password']

        #user=Instructor(name,fathers_name,aadhar,mobile,dob,email,joblocation,qualification,address,experiance,city,resume,profile,pic1,pic2,pic3,pic4)
        #user.save()
        return redirect('loginapp')
    else:
        return render(request,'register.html')


    return render(request,'register.html')
def registerstudent(request):
    return render(request,'regstudent.html')
