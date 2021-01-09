from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Userregister(models.Model):
    #user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default="")
    fathers_name = models.CharField(max_length=20, default="")
    aadhar = models.IntegerField(default='0')
    address = models.CharField(max_length=20, default="")
    city = models.CharField(max_length=50, default="")
    profile = models.ImageField(upload_to="yogbookingapp/images")
    proffession = models.CharField(max_length=20, default="")
    gender = models.CharField(max_length=5, default=0)
    def __str__(self):
        return self.name
class Instructor(models.Model):
        user = models.OneToOneField(User,on_delete=models.CASCADE)
        name = models.CharField(max_length=20, default="")
        fathers_name = models.CharField(max_length=20, default="")
        aadhar = models.IntegerField(default='0')
        mobile = models.IntegerField(default=0)
        dob = models.DateField(blank=True, null=True)
        email = models.EmailField(default="")
        joblocation = models.CharField(max_length=100,default="")
        qualification = models.CharField(max_length=200,default="")
        address = models.CharField(max_length=20, default="")
        experiance = models.CharField(max_length=20, default="")
        city = models.CharField(max_length=50, default="")
        resume = models.FileField(upload_to='yogbookingapp/pdf',default="")
        profile = models.ImageField(default="",upload_to="yogbookingapp/images")
        pic1 = models.ImageField(default="",upload_to="yogbookingapp/images")
        pic2 = models.ImageField(default="",upload_to="yogbookingapp/images")
        pic3 = models.ImageField(default="",upload_to="yogbookingapp/images")
        pic4 = models.ImageField(default="",upload_to="yogbookingapp/images")
        rating = models.IntegerField(default=0)
        def __str__(self):
            return self.name
