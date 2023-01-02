from django.shortcuts import render

def index(request):
    return render(request, 'spices/index.html')

def shop(request):
    return render(request, 'spices/shop.html')

def about(request):
    return render(request, 'spices/about.html')