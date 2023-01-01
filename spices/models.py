import datetime

from django.db import models
from django.utils import timezone

'''Create a class called Product that inherits from models.Model.'''
class Product(models.Model):
    '''Create a CharField called name that has a max_length of 255.'''
    name = models.CharField(max_length=255)
    '''Create a TextField called description.'''
    description = models.TextField()
    '''Create a DecimalField called price that has a max_digits of 6 and a decimal_places of 2.'''
    price = models.DecimalField(max_digits=6, decimal_places=2)
    '''Create an ImageField called image that has an upload_to of products/.'''
    image = models.ImageField(upload_to='products/')
    '''Create a PositiveIntegerField called inventory.'''
    inventory = models.PositiveIntegerField()
    '''Create a BooleanField called available that has a default value of True.'''
    available = models.BooleanField(default=True)
    '''Create a DateTimeField called created_at that has auto_now_add set to True.'''
    created_at = models.DateTimeField(auto_now_add=True)
    '''Create a DateTimeField called updated_at that has auto_now set to True.'''
    updated_at = models.DateTimeField(auto_now=True)

    '''Create a __str__ method that returns self.name.'''
    def __str__(self):
        return self.name