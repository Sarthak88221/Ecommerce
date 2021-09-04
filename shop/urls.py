
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contactUs"),
    path('shop/', views.shop, name="shop"),
    path('brand/', views.brand, name="brand"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('product_d/', views.product_detail, name="product_detail"),
    path('tracker/', views.tracker, name="TrackingStatus"),
    path('search/', views.search, name="Search"),
    path('productview/', views.productview, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
  
]
