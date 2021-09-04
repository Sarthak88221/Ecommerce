from django.db import models
from django.db.models.base import Model
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
from django.utils import translation, tree
from .helpers import *


# Create your models here.
class  Category(models.Model):
    title= models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.title


class Customer(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE, null=True,blank=True)
    name= models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=50,default ="")
    slug =models.SlugField(max_length=1000, null=True,blank=True)
    price = models.IntegerField(default =0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default ="")

    def __str__(self):
         return self.product_name

    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.product_name)
        super(Product,self).save(*args,**kwargs)

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url        


class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_order=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
     
    def __str__(self):
        return str(self.id)

class Order_items(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity= models.IntegerField(default=0,null=True)     
    date_added = models.DateField(auto_now_add=True)

class Ship_add(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)   
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)   
    address=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    zipcode=models.CharField(max_length=100,null=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.address