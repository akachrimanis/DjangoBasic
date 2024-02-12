from django.db.models import (CharField,BooleanField,IntegerField,EmailField,TextField,DateTimeField)

from django.db import models

# Create your models here.
class Customer(models.Model):
    name = CharField(max_length=100,verbose_name="Company Name",)
    active = BooleanField(default=False,verbose_name="Active",)
    AFM = IntegerField(blank=True,null=True,verbose_name="AFM",)
    contact_first_name = CharField(max_length=100,verbose_name="First Name",)
    contact_last_name = CharField(max_length=100,verbose_name="Last Name",)
    email = EmailField(unique=True,verbose_name="Email",)
    phone = CharField(max_length=15,blank=True,null=True,verbose_name="Phone",)
    address = TextField(blank=True,null=True,verbose_name="Address",)
    created_at = DateTimeField(auto_now_add=True,verbose_name="Created at",)
    updated_at = DateTimeField(auto_now=True,verbose_name="Updated at",)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


