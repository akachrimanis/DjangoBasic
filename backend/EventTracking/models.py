from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

from CustomerB2B.models import CustomerB2B
from CustomerB2C.models import CustomerB2C
from Product.models import Product
    
    
    

class UserSession(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)#Linktotheuser,if 
    session_key = models.CharField(max_length=40) 
    start_time = models.DateTimeField(auto_now_add=True) 
    end_time = models.DateTimeField(null=True,blank=True) 
    ip_address = models.CharField(max_length=20) 
    history = HistoricalRecords() 


class Event(models.Model):
    user_session = models.ForeignKey(UserSession,on_delete=models.CASCADE) 
    event_type = models.CharField(max_length=100)#e.g.,'page_visit','button_click' 
    timestamp = models.DateTimeField(auto_now_add=True) 
    details = models.TextField()#JSONstringforadditionaleventdetails 
    history = HistoricalRecords() 


class UserDevice(models.Model):
    user_session = models.ForeignKey(UserSession,on_delete=models.CASCADE) 
    device_details = models.TextField()#e.g.,'page_visit','button_click' 
    timestamp = models.DateTimeField(auto_now_add=True) 
    history = HistoricalRecords() 


class PageView(models.Model):
    user_session = models.ForeignKey(UserSession,on_delete=models.CASCADE) 
    url = models.URLField()#e.g.,'page_visit','button_click' 
    timestamp = models.DateTimeField(auto_now_add=True) 
    history = HistoricalRecords() 


class ClickEvent(models.Model):
    user_session = models.ForeignKey(UserSession,on_delete=models.CASCADE) 
    element_id = models.CharField(max_length=100)#IDoftheclickedelement 
    timestamp = models.DateTimeField(auto_now_add=True) 
    history = HistoricalRecords() 


class SearchQuery(models.Model):
    user_session = models.ForeignKey(UserSession,on_delete=models.CASCADE) 
    query = models.TextField()#IDoftheclickedelement 
    timestamp = models.DateTimeField(auto_now_add=True) 
    history = HistoricalRecords() 


class UserPreference(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    preferences = models.JSONField()#StorespreferencesasaJSONobject 
    history = HistoricalRecords() 


class CartActivity(models.Model):
    user_session = models.ForeignKey(UserSession,on_delete=models.CASCADE) 
    activity_type = models.CharField(max_length=100)#e.g.,'add_to_cart','remove_from_cart'aJSONobject 
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 
    quantity = models.IntegerField() 
    timestamp = models.DateTimeField(auto_now_add=True) 
    history = HistoricalRecords() 


class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    product = models.ForeignKey(Product,on_delete=models.CASCADE)#StorespreferencesasaJSONobject 
    added_on = models.DateTimeField(auto_now_add=True) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    history = HistoricalRecords() 


class UserFeedback(models.Model):
    user_session = models.ForeignKey(UserSession,on_delete=models.CASCADE) 
    feedback = models.TextField()#StorespreferencesasaJSONobject 
    timestamp = models.DateTimeField(auto_now_add=True) 


class ErrorLog(models.Model):
    user_session = models.ForeignKey(UserSession,on_delete=models.CASCADE) 
    error_message = models.TextField()#StorespreferencesasaJSONobject 
    timestamp = models.DateTimeField(auto_now_add=True) 

