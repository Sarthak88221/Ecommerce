from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')


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
def checkout(request):
    return HttpResponse("checkout page")