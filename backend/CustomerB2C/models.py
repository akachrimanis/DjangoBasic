from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

    
    
    

class CustomerB2C(models.Model):
    firstname = models.CharField(max_length=100) 
    surname = models.CharField(max_length=100) 
    date_of_birth = models.DateField() 
    email = models.EmailField(blank=True,null=True) 
    phone = models.CharField(max_length=20,blank=True,null=True) 
    website = models.URLField(blank=True,null=True) 
    address_line_1 = models.CharField(max_length=255,blank=True,null=True) 
    address_line_2 = models.CharField(max_length=255,blank=True,null=True) 
    city = models.CharField(max_length=100,blank=True,null=True) 
    state = models.CharField(max_length=100,blank=True,null=True) 
    postal_code = models.CharField(max_length=20,blank=True,null=True) 
    country = models.CharField(max_length=100,blank=True,null=True) 
    notes = models.TextField(blank=True,null=True) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    history = HistoricalRecords() 


class CustomerUserProfileB2C(models.Model):
    username = models.CharField(max_length=100) 
    firstname = models.CharField(max_length=100) 
    surname = models.CharField(max_length=100) 
    email = models.EmailField() 
    phone = models.CharField(max_length=20, blank=True, null=True) 
    last_login = models.DateTimeField(auto_now=True) 
    history = HistoricalRecords() 

