from django.contrib import admin
from django.urls import path,include
from . import views
admin.site.site_header="Yogbooking.com"
admin.site.site_title="Welcome To Yogbooking.com"
admin.site.index_title="Yogbooking.com"
urlpatterns = [
    path('',views.index,name='index'),
    path('services',views.services,name = 'services'),
    path('about/',views.about,name = 'about'),
    path('Contact/',views.contact,name = 'contact'),
    path('Events/',views.events,name = 'event'),
    path('shop/',views.shop,name = 'shop'),
    path('dailyyoga',views.dailyyoga,name="dailyyoga"),
    path('onlineyogaclasses',views.onlineyoga,name="onlineyoga"),
    path('monthlyyogapackage',views.monthlyyoga,name="monthlyyoga"),
    path('halfyearlyogapackage',views.halfyearlyoga,name="halfyearlyyoga"),
    path('annualyogapackage',views.annualyogapackage,name="annualpackage"),
    path('groupyoga',views.groupyoga,name="groupyoga"),
    path('parkyoga',views.parkyoga,name="parkyoga"),
    path('kidyoga',views.kidyoga,name="kidyoga"),
    path('BookNow',views.bookinstructor,name="bookinstructor"),
    path('Dashboard',views.dashboard,name = 'dashboard'),
    path('Success',views.success,name='success')

]
