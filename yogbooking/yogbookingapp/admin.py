from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Services)
admin.site.register(models.Booking)
admin.site.register(models.Blog)
admin.site.register(models.Events)
admin.site.register(models.Upcommingevent)
#admin.site.register(User,UserAdmin)
