from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'image', 'inventory', 'available', 'updated_at']

admin.site.register(Product, ProductAdmin)
