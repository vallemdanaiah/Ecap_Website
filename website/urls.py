"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from website import views as mainview
from admins import views as adminviews
from Ecap import views as userviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainview.index, name='index'),
    path('logout', mainview.logout, name='logout'),
    path('STUDENTREGISTERFORM', mainview.STUDENTREGISTERFORM, name='STUDENTREGISTERFORM'),
    path('STUDENTLOGIN', mainview.STUDENTLOGIN, name='STUDENTLOGIN'),
    path('ADMINLOGIN', mainview.ADMINLOGIN, name='ADMINLOGIN'),
    
    #admin views
    path('AdminLoginCheck', adminviews.AdminLoginCheck, name='AdminLoginCheck'),
    path('addstudent', adminviews.addstudent, name='addstudent'),
    path('addstudentlist', adminviews.addstudentlist, name='addstudentlist'),
    path('adminindex', adminviews.adminindex, name='adminindex' ),
    
    
    #user views 
    path('UserHome', userviews.UserHome, name='UserHome' ),
    path('userlogin', userviews.userlogin, name='userlogin'),
    path('search', userviews.search, name='search'),
    path('UserRegisterActions', userviews.UserRegisterActions, name='UserRegisterActions')
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


