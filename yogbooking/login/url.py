from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.loginpage, name="login"),
    path('Register',views.register, name="register"),
    path('ApplyStudent',views.registerstudent,name="registerstudent")
]
