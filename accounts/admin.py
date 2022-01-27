from django.contrib import admin

# Register your models here.
# from .models import Customer, Product, Order
from .models import *  #instead we use * to import all

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)