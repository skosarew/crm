from django.shortcuts import render
from .models import Product, Order, Customer


# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = customers.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, 'accounts/dashboard.html', context)


def products(requst):
    products = Product.objects.all()
    return render(requst, 'accounts/products.html', {'products': products})


def customer(request):
    return render(request, 'accounts/customer.html')
