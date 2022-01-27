from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    outfordelivery = orders.filter(status='Out for delivery').count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers, 'total_customers': total_customers,
               'total_orders': total_orders, 'delivered': delivered, 'pending': pending,
               'outfordelivery': outfordelivery}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()

    # Below first product is the key and second one is the value. They key we pass in our html templates and value we
    # get from this function in the above line of code.
    return render(request, 'accounts/products.html', {'products': products})


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'orders_count': order_count}
    return render(request, 'accounts/customer.html', context)

def customers(request):
    customers = Customer.objects.all()
    customers_count = customers.count()
    orders = Order.objects.all()
    total_orders = Order.objects.all().count()
    context = {'customers': customers, 'customers_count': customers_count, 'total_orders': total_orders, 'orders': orders}
    return render(request, 'accounts/customers.html', context)