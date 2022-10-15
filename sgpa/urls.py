from django.urls import path
from . import views 

urlpatterns = [
    path('',views.sgpa,name='sgpa'),
    path('sgpaselect/<int:sem>/',views.sgpaselect,name='sgpaselect'),
    path('sgpaselect/<str:sem>/',views.csec,name='csec'),
]
