from django.contrib import admin
from django.urls import path
from . import views
from demoapp.views import *
urlpatterns = [
  
    path('login', views.loginpage, name='login'),
    path('register1', views.registerpage, name='register1'),
    path('logout',views.logoutuser, name='logout'),
]
