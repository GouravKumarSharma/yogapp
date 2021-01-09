from django.contrib import admin
from . import models

from django.contrib.auth.admin import UserAdmin as BaseUser
from django.contrib.auth.models import User
from login.models import Instructor


class Instructor(admin.StackedInline):
    model = Instructor
    can_delete = False
    verbose_name_plural='instructor'

#define User
class UserAdmin(BaseUser):
    inline = (Instructor,)


# Register your models here.

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(models.Userregister)
admin.site.register(models.Instructor)
