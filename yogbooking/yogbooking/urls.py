
from django.contrib import admin
from django.urls import path,include
from yogbookingapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('yogbookingapp/',include('yogbookingapp.url'),name='yogbookingapp'),
    path('login/',include('login.url'),name='login'),
]
