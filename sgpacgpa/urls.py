
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = 'index'),
    path('cgpa/',include('cgpa.urls')),
    path('sgpa/',include('sgpa.urls')),
    path('signup/',views.signup,name="signup"),
path('login/',views.login,name="login"),
]
