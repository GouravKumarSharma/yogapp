from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Instructor
# Very Basic Example of a Django Form


class Instructorlogin(forms.ModelForm):
    name = forms.CharField(label='name', max_length=100)
    fathers_name = forms.CharField(label='fathers name', max_length=100)
    address = forms.CharField(label='Address', max_length=100)
    mobile = forms.IntegerField(label='Address')
    dob = forms.DateField(label='Address')
    email = forms.EmailField(label='Address' )
    joblocation = forms.CharField(label='Address', max_length=100)
    qualification = forms.CharField(label='Address',max_length=200)
    address = forms.CharField(label='Address', max_length=20)
    experiance = forms.CharField(label='Address', max_length=20)
    city = forms.CharField(label='Address', max_length=50)
    resume = forms.FileField(
        label='Resume')

    class Meta:
        model = Instructor
        fields = ["name", "fathers_name", "address",
                  "mobile", "dob", "email", "joblocation",
                   "qualification", "city", "experiance", "resume", "city",
                   ]
   
class LoginForm(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())
   def clean_message(self):
       username = self.cleaned_data.get("username")
       dbuser = Instructor.objects.filter(name = username)
       if not dbuser:
           raise forms.ValidationError("User does not exist in our db!")
       return username
