from django.shortcuts import render
import pandas as pd
import json
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px
# from django.http import JsonResponse
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'spices/index.html', {'products': products})

def shop(request):
    products = Product.objects.all()
    return render(request, 'spices/shop.html', {'products': products})

def about(request):
    return render(request, 'spices/about.html')

def viz(request):
    data = px.scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13],)
    data.update_traces(marker=dict(color='red', size=10))

    graph_json = json.dumps(data, cls=PlotlyJSONEncoder)

    return render(request, 'spices/viz.html', {'graph_json': graph_json})