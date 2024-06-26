from django.contrib import admin
from .models import Category,ProductList
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','description']

class ProductAdmin(admin.ModelAdmin):
    list_display=['product_title','product_price','product_description','product_count','product_rating','product_image']

admin.site.register(Category,CategoryAdmin)
admin.site.register(ProductList,ProductAdmin)

