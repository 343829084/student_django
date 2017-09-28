"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#-*-coding:utf-8-*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    #(r'^grappelli/',include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^accounts/login/$', 'webadmin.account.userlogin',name="userlogin"),
    url(r'^$', 'webadmin.views.index', name='home'),
    url(r'^accounts/login/$', 'webadmin.account.userlogin',name="userlogin"),
    url(r'^accounts/login/$', 'webadmin.account.userlogin',name="userlogin"),
    url(r'^accounts/changepassword/$', 'webadmin.account.changepassword',name="changepassword"),
    url(r'^accounts/logout/$',  'django.contrib.auth.views.logout', {'next_page': '/accounts/login/'},name="userlogout"),
    
    #student
    url(r'^studentprofile/$', 'webadmin.student.studentprofile',name="studentprofile"),

]
