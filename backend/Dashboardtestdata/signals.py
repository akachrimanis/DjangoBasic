def create_signals(df, model_name):
    
    context = f"""
    
from django.db.models.signals import post_save 
from django.dispatch import receiver 
from .models import {model_name}, {model_name}Aggregates 

@receiver(post_save, sender={model_name}) 
def update_{model_name.lower()}_aggregates(sender, instance, created, **kwargs): 
    if created: 
        {model_name}Aggregates.objects.create(total_{model_name.lower()}s=1) 
    else: 
        aggregates = {model_name}Aggregates.objects.first() 
        aggregates.total_customers = {model_name}.objects.count() 
        aggregates.save()
    """
    return context


