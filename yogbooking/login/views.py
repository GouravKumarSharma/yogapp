from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout,login,authenticate
from django.views.decorators.csrf import csrf_exempt, csrf_protect
#from login.form import Instructorregister
from login.form import LoginForm,Instructorlogin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Instructor
from django.http import HttpResponse
from . import orderid
import razorpay


# Create your views here.
def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "loginapp.html",
                    context={"form":form})

def logout_view(request):
    logout(request)
    return redirect('/')
        #user=Instructor(name,fathers_name,aadhar,mobile,dob,email,joblocation,qualification,address,experiance,city,resume,profile,pic1,pic2,pic3,pic4)
        #user.save()
       # return redirect('loginapp')
    #else:
        #return render(request,'register.html')


    #return render(request,'register.html')
def registerstudent(request):
    return render(request,'regstudent.html')

def register(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        name = request.POST['name']
        fathers_name = request.POST['fname']
        aadhar = request.POST['aadhar']
        mobile = request.POST['mobile']
        dob = request.POST['dob']
        email = request.POST['email']
        joblocation = request.POST['joblocation']
        qualification = request.POST['qualification']
        city = request.POST['city']
        resume = request.POST['resume']
        profile = request.POST['profile']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        address = request.POST['address']
        exp = request.POST['exp']
        pic1 = request.POST['pic1']
        pic2 = request.POST['pic2']
        pic3 = request.POST['pic3']
        pic4 = request.POST['pic4']
        print('get data...')
        instructor = Instructor.objects.create(
            name = name,
            fathers_name = fathers_name,
            aadhar = aadhar,
            mobile = mobile,
            dob = dob,
            user = email,
            joblocation=joblocation,
            qualification = qualification,
            city = city,
            resume = resume,
            profile = profile,
            password = password,
            address=address,
            experiance = exp,
            pic1 = pic1,
            pic2=pic2,
            pic3=pic3,
            pic4=pic4
        )
        
        instructor.save()
        print('data saved..')
        return redirect('/')

    else:
        return render(request,'register.html')
   
