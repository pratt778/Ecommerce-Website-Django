from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
@method_decorator(login_required(login_url='login'),name='dispatch')
class home(View):
    def get(self,request):
        return render(request,'index.html')