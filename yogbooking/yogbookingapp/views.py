from django.shortcuts import render
from .models import Services,Events,Upcommingevent
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
    return render(request,'yogbookingapp/booknow.html',{'services' : services})
