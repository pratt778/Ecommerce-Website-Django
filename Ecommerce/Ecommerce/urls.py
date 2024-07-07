"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from EHome.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.as_view(),name='home'),
    path('auth/',include('authenticate.urls')),
    path('product-info/<pid>',productinfo.as_view(),name="productinfo"),
    path('category/<int:cid>',categoryinfo.as_view(),name="category"),
    path('search/',search.as_view(),name='search'),
    path('ratings/',ratings.as_view(),name="ratings"),
    path('userdetails/',userdetails.as_view(),name="userdetail"),
    path('mycart/<pid>',myCart.as_view(),name="mycart"),
    path('sort/<str:so>',mysort.as_view(),name="sort"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
