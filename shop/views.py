from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def brand(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'shop2.html',context)
def product_detail(request):
    return render(request,'product_d.html')
def cart(request):
    return render(request,'Cart.html')
def checkout(request):
    return render(request,'checkout.html')


def contact(request):
    return HttpResponse("Contact page")
def shop(request):
    return render(request,'shop.html')
def tracker(request):
    return HttpResponse("Tracker page")
def search(request):
    return HttpResponse("search page")
def productview(request):
    return HttpResponse("productview page")
