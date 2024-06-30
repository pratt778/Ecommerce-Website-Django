
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import requests
from .models import ProductList,Category
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
# Create your views here.
@method_decorator(login_required(login_url='login'),name='dispatch')
class home(View):
    def fetch(self,request):
        myrequest = requests.get('https://fakestoreapi.com/products')
        if myrequest.status_code == 200:
            return myrequest.json()
        else:
            return "some error occured"
    
    def save_products(self,products):
        for product in products:
            cname = product['category']
            category,created = Category.objects.get_or_create(name=cname,description="this is description")
            ProductList.objects.update_or_create(
                product_id=product['id'],
                defaults={
                    'product_title':product['title'],
                    'product_price':product['price'],
                    'product_description':product['description'],
                    'Category':category,
                    'product_image':product['image'],
                    'product_rating':product['rating']['rate'],
                    'product_count':product['rating']['count'],
                }
            )

    def get(self,request):
        data={}
        # getvalues = self.fetch(request)
        # if getvalues:
        #     self.save_products(getvalues)
        myproduct = ProductList.objects.all()
        mycategory = Category.objects.all()
        products = ProductList.objects.all()
        # for pro in products:
        #     print(pro.product_rating)
            
        data['product']=myproduct
        data['category']=mycategory
        return render(request,'index.html',data)


class productinfo(View):
    def get(self,request,pid):
        data={}
        myproduct=ProductList.objects.get(product_id=pid)
        data['product']=myproduct
        price = myproduct.product_price
        data['price']=float(price-15)
        return render(request,'product-detail.html',data)
    
class categoryinfo(View):
    def get(self,request,cid):
        data={}
        mycat = Category.objects.get(id = cid)
        myproducts = ProductList.objects.filter(Category=mycat)
        data['product']=myproducts
        cate = Category.objects.all()
        data['category']=cate
        data['cid']=cid
        return render(request,'category-detail.html',data)
    
class search(ListView):
    model=ProductList
    template_name="product-list.html"
    context_object_name='product'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return ProductList.objects.filter(product_title__icontains=query)
        else:
            return ProductList.objects.none()
        
    
class ratings(View):
    def get(self,request):
        data={}
        myrating = request.GET.get('star')
        myproduct=ProductList.objects.filter(product_rating__gte=(float(myrating))).order_by('product_rating')
        data['product']=myproduct
        return render(request,'product-list.html',data)

class userdetails(View):
    def get(self,request):
        data={}
        myuser=User.objects.get(username=request.user)
        data['user']=myuser
        return render(request,'user-details.html',data)
    
class myCart(View):
    def get(self,request,pid):
        return render(request,"mycart.html")
    
class mysort(View):
    def get(self,request,so):
        data={}
        if so=='asc':
            myproduct=ProductList.objects.all().order_by('product_price')
        elif so=='desc':
            myproduct=ProductList.objects.all().order_by('-product_price')
        data['product']=myproduct
        data['vals']=so
        return render(request,"product-list.html",data)