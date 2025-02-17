from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request=request,template_name='index.html')

def login(request):
    return render(request=request,template_name='login.html')

def register(request):
    return render(request=request,template_name='register.html')

def logout(request):
    return render(request=request,template_name='index.html')

def comunidade(request):
    return render(request=request,template_name='comunidade.html')