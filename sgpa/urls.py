from django.urls import path

urlpatterns = [
    path('',views.sgpa,name='sgpa'),
    path('sgpaselect/',views.sgpaselect,name='sgpaselect'),
]
