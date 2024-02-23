from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

from CustomerB2B.models import CustomerB2B
from CustomerB2C.models import CustomerB2C
from Product.models import Product
    
    
    

class Dashboard(models.Model):
    date = models.DateTimeField(blank=False, null=False) 
    price = models.IntegerField(blank=False, null=False) 
    created_at = models.DateTimeField(blank=False, null=False) 
    updated_at = models.DateTimeField(blank=False, null=False) 

