from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name

class ProductList(models.Model):
    product_id = models.IntegerField(unique=True)
    product_title = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_description=models.TextField()
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_image=models.URLField()
    product_rating = models.FloatField()
    product_count=models.IntegerField()

    def __str__(self):
        return self.product_title
    
class AddtoCart(models.Model):
    product = models.ForeignKey(ProductList,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total_price(self):
        return self.quantity * self.product.product_price
    def __str__(self):
        return self.product.product_title

