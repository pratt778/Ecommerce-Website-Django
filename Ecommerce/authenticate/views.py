from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm,LoginForm
from django.http import HttpResponse
from .decorators import redirect_authenticated_users
from django.utils.decorators import method_decorator

# Create your views here.

class SignUp(View):
    @method_decorator(redirect_authenticated_users)
    def get(self,request):
        template_name='register.html'
        data={}
        form = RegisterForm()
        data['form']=form
        return render(request,template_name,data)
    @method_decorator(redirect_authenticated_users)
    def post(self,request):
        myform = RegisterForm(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('login')
        else:
            return HttpResponse('form is not valid')
        
    
#def Signin(request):
#     return render(request,'register.html')

class LogIn(View):
    @method_decorator(redirect_authenticated_users)
    def get(self,request):
        template_name='login.html'
        data={}
        myform = LoginForm()
        data['form']=myform
        return render(request,template_name,data)
    @method_decorator(redirect_authenticated_users)
    def post(self,request):
        myform = LoginForm(request.POST)
        if myform.is_valid():
            username = myform.cleaned_data['username']
            password = myform.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse('error occurred in user')
        else:
            return HttpResponse('form is not valid')
        
class LogOut(View):
    def get(self,request):
        logout(request)
        return redirect('login')
        