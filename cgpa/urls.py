from django.urls import path
from . import views

urlpatterns = [
    path('',views.cgpa,name='cgpa'),
    path("result/",views.result, name="result"),
    
]
