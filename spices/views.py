from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'spices/index.html', {'products': products})

def shop(request):
    products = Product.objects.all()
    return render(request, 'spices/shop.html', {'products': products})

def about(request):
    return render(request, 'spices/about.html')