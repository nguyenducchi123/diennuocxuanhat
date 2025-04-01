from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm
    return render(request, 'home/index.html', {'products': products})

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def products(request):
    return render(request, 'home/products.html')

def services(request):
    return render(request, 'home/services.html')