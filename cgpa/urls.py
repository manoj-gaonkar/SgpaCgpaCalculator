from django.urls import path

urlpatterns = [
    path('',views.cgpa,name='cgpa'),
    path("result/",views.result, name="result"),
    
]
