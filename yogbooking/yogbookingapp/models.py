from django.db import models
#import User

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=50, default='')
    price = models.IntegerField(default='0')
    description = models.CharField(max_length=1000,default="")
    id = models.CharField(max_length=20,default="",primary_key = True)
    image = models.ImageField(upload_to="yogbookingapp/images")
    def __str__(self):
        return self.name
class Events(models.Model):
    name = models.CharField(max_length=20, default="")
    description = models.CharField(max_length=1000,default="")
    image = models.ImageField(upload_to="images")
    def __str__(self):
        return self.name
class Blog(models.Model):
    name = models.CharField(max_length=20, default="")
    img1 = models.ImageField(upload_to="yogbookingapp/images")
    img2 = models.ImageField(upload_to="yogbookingapp/images")
    text = models.CharField(max_length=2000, default="")
    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=50, default="")
    mobile = models.IntegerField(default=0)
    email = models.EmailField(default = "none")
    injury = models.CharField(max_length=50, default="")
    #city = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=20, default="")
    no_of_students = models.IntegerField(default=0)
    date_of_event = models.DateField(blank=True, null=True,default = "none")
    service = models.CharField(max_length=50, default="")
    msg = models.CharField(max_length=200,default='')
    payment_id=models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name
class Upcommingevent(models.Model):
    name = models.CharField(max_length=50,default="")
    date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="yogbookingapp/images")
    id = models.CharField(max_length=30,primary_key = True)
    def __str__(self):
        return self.name
