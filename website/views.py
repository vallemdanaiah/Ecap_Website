from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html',{})


def STUDENTREGISTERFORM(request):
    return render(request,'STUDENTREGISTERFORM.html',{})


def STUDENTLOGIN(request):
    return render(request,'STUDENTLOGIN.html',{})


def ADMINLOGIN(request):
    return render(request,'ADMINLOGIN.html')










def logout(request):
    return render(request,'index.html')
