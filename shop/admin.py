from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Order_items)
admin.site.register(Ship_add)
