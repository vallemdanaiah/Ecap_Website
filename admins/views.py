from django.shortcuts import render
from django.contrib import messages
from .models import StdDetailes
from .forms import StdDetailesForm


# Create your views here.
def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return render(request, 'admins/AdminHome.html')
        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'ADMINLOGIN.html', {})


def addstudent(request):    
    if request.method == 'POST':    
        form = StdDetailesForm(request.POST,request.FILES)            
        if form.is_valid():           
            form.save()              
            form = StdDetailesForm()              
            return render(request,'admins/addstudent.html',{'form':form,'msg':'sucessfully add'})                 
        else:
            return render(request,'admins/addstudent.html',{'form':form,'msg':'sucessfully add'})
    else:
        form = StdDetailesForm()   
    return render(request,'admins/addstudent.html',{'form':form,'msg':'sucessfully add'})
         
    
    
from .models import StdDetailes
def addstudentlist(request):
    data = StdDetailes.objects.all()
    return render(request,'admins/addstudentlist.html',{'data':data})




def adminindex(request):
    return render(request,'admins/AdminHome.html',{})