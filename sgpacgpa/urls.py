
from django.contrib import admin
from django.urls import path
from . import views
from cgpa.views import cgpa
from sgpa.views import sgpa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = 'index'),
    path('cgpa/',cgpa,name='cgpa'),
    path('sgpa/',sgpa,name='sgpa')

]
