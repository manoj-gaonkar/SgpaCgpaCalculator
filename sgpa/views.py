from django.shortcuts import render

def sgpa(request):
    return render(request,'sgpa/sgpa.html')

def sgpaselect(request):
    return render(request,'sgpa/sgpasem.html')
    
