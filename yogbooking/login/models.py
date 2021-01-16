from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Instructor(models.Model):

        #user = models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE)
        name = models.CharField(max_length=20, default="")
        fathers_name = models.CharField(max_length=20, default="")
        aadhar = models.IntegerField(default='0')
        mobile = models.IntegerField(default=0)
        dob = models.DateField(blank=True, null=True)
        user = models.EmailField(default="")
        joblocation = models.CharField(max_length=100,default="")
        qualification = models.CharField(max_length=200,default="")
        address = models.CharField(max_length=200, default="")
        experiance = models.CharField(max_length=20, default="")
        city = models.CharField(max_length=50, default="")
        resume = models.FileField(upload_to='login/pdf',default="")
        profile = models.ImageField(default="",upload_to="login/images")
        pic1 = models.ImageField(default="",upload_to="login/images")
        pic2 = models.ImageField(default="",upload_to="login/images")
        pic3 = models.ImageField(default="",upload_to="login/images")
        pic4 = models.ImageField(default="",upload_to="login/images")
        rating = models.IntegerField(default=0)
        password = models.CharField(max_length=50,default="")
        def __str__(self):
            return self.name
