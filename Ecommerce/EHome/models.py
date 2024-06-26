from django.db import models

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
