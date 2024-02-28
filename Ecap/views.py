from django.shortcuts import render
from django.contrib import messages
from .models import UserRegistrationModel
from .forms import UserRegistrationModelForm

# Create your views here.



def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationModelForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationModelForm()
            return render(request, 'STUDENTREGISTERFORM.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationModelForm()
    return render(request, 'STUDENTREGISTERFORM.html', {'form': form})

def userlogin(request):
    if request.method == 'POST':
        loginid = request.POST.get('loginid')
        print(loginid)#debugging
        password = request.POST.get('password')
        print(password)#debugging
        print('loginid=', loginid, 'password=', password)  # Debugging print statement
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=password)
            print('Found user:', check)  # Debugging print statement
            return render(request, 'users/UserHomePage.html', {})
        except UserRegistrationModel.DoesNotExist:
            print('User not found')  # Debugging print statement
            messages.error(request, 'Invalid name and email')
    return render(request, 'STUDENTLOGIN.html', {})


from admins.models import StdDetailes

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = StdDetailes.objects.filter(stdname__icontains=query)
    return render(request, 'users/UserBase.html', {'results': results, 'query': query})






# def UserLoginCheck(request):
#     if request.method == "POST":
#         loginid = request.POST.get('loginid')
#         pswd = request.POST.get('pswd')
#         print("Login ID = ", loginid, ' Password = ', pswd)
#         try:
#             check = UserRegistrationModel.objects.get(
#                 loginid=loginid, password=pswd)
#             status = check.status
#             print('Status is = ', status)
#             if status == "activated":
#                 request.session['id'] = check.id
#                 request.session['loggeduser'] = check.name
#                 request.session['loginid'] = loginid
#                 request.session['email'] = check.email
#                 print("User id At", check.id, status)
#                 return render(request, 'users/UserHomePage.html', {})
#             else:
#                 messages.success(request, 'Your Account Not at activated')
#                 return render(request, 'UserLogin.html')
#         except Exception as e:
#             print('Exception is ', str(e))
#             pass
#         messages.success(request, 'Invalid Login id and password')
#     return render(request, 'UserLogin.html', {})


def UserHome(request):
    return render(request, 'users/UserHomePage.html', {})



# def index(request):
#     return render(request,'index.html',{})


# def STUDENTREGISTERFORM(request):
#     return render(request,'STUDENTREGISTERFORM.html',{})


# def STUDENTLOGIN(request):
#     return render(request,'STUDENTLOGIN.html',{})


# def ADMINLOGIN(request):
#     return render(request,'ADMINLOGIN.html')










# def logout(request):
#     return render(request,'index.html')
