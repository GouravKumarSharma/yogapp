
from django.contrib import admin
from django.urls import path,include
from yogbookingapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('yogbookingapp/',include('yogbookingapp.url'),name='yogbookingapp'),
    path('login/',include('login.url'),name='login'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
