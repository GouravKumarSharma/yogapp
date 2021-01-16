from django.shortcuts import render, redirect
from .models import Services,Events,Upcommingevent,Booking
import razorpay
from . import orderid

# Create your views here.
def index(request):
    services = Services.objects.all()

    return render(request, 'yogbookingapp/index.html',{'services' : services})
def services(request):
    services = Services.objects.all()

    return render(request,'yogbookingapp/services.html',{'services' : services})
def events(request):
    events = Events.objects.all()
    upcommingevent = Upcommingevent.objects.all()
    return render(request,'yogbookingapp/eventpage.html',{'events' : events})
def about(request):
    return render(request,'yogbookingapp/about.html')
def contact(request):
    return render(request,'yogbookingapp/contact.html')
def shop(request):
    return render(request,'yogbookingapp/shop.html')
def dailyyoga(request):
    services = Services.objects.filter(id = 'dailyyoga')
    return render(request,'yogbookingapp/service.html',{'services' : services})
def onlineyoga(request):
    services = Services.objects.filter(id = 'onlineyoga')
    return render(request,'yogbookingapp/service.html',{'services' : services})
def monthlyyoga(request):
    services = Services.objects.filter(id = 'monthlyyoga')
    return render(request,'yogbookingapp/service.html',{'services' : services})
def halfyearlyoga(request):
    services = Services.objects.filter(id = 'halfyearlyyoga')
    return render(request,'yogbookingapp/service.html',{'services' : services})
def annualyogapackage(request):
    services = Services.objects.filter(id = 'annualpackage')
    return render(request,'yogbookingapp/service.html',{'services' : services})
def groupyoga(request):
    services = Services.objects.filter(id = 'groupyoga')
    return render(request,'yogbookingapp/service.html',{'services' : services})
def parkyoga(request):
    services = Services.objects.filter(id = 'parkyoga')
    return render(request,'yogbookingapp/service.html',{'services' : services})
def kidyoga(request):
    services = Services.objects.filter(id = 'kidyoga')
    return render(request,'yogbookingapp/service.html',{'services' : services})
def bookinstructor(request):
    services = Services.objects.all()
    if request.method=='POST':
        #order_amount = 29900
        #order_currency = 'INR'
        order_receipt = orderid.orderid
        name = request.POST['name']
        noofpeople = request.POST['noofpeople']
        date = request.POST['date']
        mobile = request.POST['mobile']
        email = request.POST['email']
        address = request.POST['address']
        injury = request.POST['injury']
        service = request.POST['item']
        msg = request.POST['message']
        booking = Booking.objects.create(
        payment_id=order_receipt,
        name = name,
        mobile = mobile,
        email = email,
        injury = injury,
        address = address,
        no_of_students = noofpeople,
        date_of_event = date,
        service = service,
        msg = msg,
        )
        booking.save()
        
        print(orderid.orderid)
        # OPTIONALclient.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)
        
        client = razorpay.Client(
            auth=('rzp_test_Dr4vACZpQp5l9V', 'EZYzh6OSYgQTIhgsKS3yLv5V'))
        payment = client.order.create(
            {'order_amount': '29900', 'order_currency': 'INR', 'receipt': 'order_receipt', 'payment_capture': '1'})

        print("jhsdkufhsudhfuhsduifgiudg")
        return redirect(success)
    else:
        print('noooooooo')
        return render(request,'yogbookingapp/booknow.html',{'services' : services})
def dashboard(request):
    return render(request,'yogbookingapp/dashboard.html')
def success(request):
    #order_receipt = n
    return render(request,'yogbookingapp/success.html')
