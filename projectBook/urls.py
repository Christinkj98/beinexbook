"""projectBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import re_path
from book_api import views

urlpatterns = [
   
    re_path(r'^$',views.login,name="login"),
    re_path(r'^booklist$',views.booklist,name="booklist"),
    re_path(r'^logout$',views.logout,name="logout"), 
    re_path(r'^admin/$',views.adminlist,name="adminlist"),
    re_path(r'^addnew/$',views.addnew,name="addnew"),
    re_path(r'^editbook/(?P<id>\d+)/$',views.editbook,name="editbook"),
    re_path(r'^deletebook/(?P<id>\d+)/$',views.deletebook,name="deletebook"),
]
