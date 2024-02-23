from django.db import models
from simple_history.models import HistoricalRecords



class InteractionType(models.Model):
    name = models.CharField(max_length=50) 


class Interaction(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE) 
    date = models.DateTimeField() 
    interaction_type = models.ForeignKey(InteractionType,on_delete=models.SET_NULL,null=True) 
    notes = models.TextField() 
    history = HistoricalRecords() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 


class InteractionDetails(models.Model):
    interaction = models.OneToOneField(Interaction,on_delete=models.CASCADE) 
    details = models.TextField() 
    handled_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='handled_interactions') 
    history = HistoricalRecords() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 


class TaskType(models.Model):
    name = models.CharField(max_length=50) 
    history = HistoricalRecords() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 


class Task(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE) 
    task_type = models.ForeignKey(TaskType,on_delete=models.SET_NULL,null=True) 
    due_date = models.DateTimeField() 
    description = models.TextField() 
    assigned_to = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='assigned_tasks') 
    history = HistoricalRecords() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

