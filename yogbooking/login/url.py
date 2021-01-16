from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.loginpage, name="login"),
    path('Register',views.register, name="register"),
    path('ApplyStudent',views.registerstudent,name="registerstudent"),
    path('logout',views.logout_view,name="logout")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
