from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('signup',SignUp.as_view(),name='signup'),
    path('login',LogIn.as_view(),name='login'),
    path('logout',LogOut.as_view(),name='logout'),
]