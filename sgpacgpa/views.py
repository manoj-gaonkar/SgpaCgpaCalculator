from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import newUserForm

def index(request):
    return render(request,'index.html')

def signup(request):
    form = newUserForm()
    context = {
        'form':form,
    }
    return render(request,'signuppage.html',context)

def login(request):
    return render(request,'loginpage.html')