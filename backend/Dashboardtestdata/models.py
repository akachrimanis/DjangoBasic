from django.db.models import (DateTimeField,IntegerField)

from django.db import models

# Create your models here.
class Dashboardtestdata(models.Model):
    date = DateTimeField(blank=False,null=False,verbose_name="Date",)
    price = IntegerField(default=False,verbose_name="Price",)
    created_at = DateTimeField(auto_now_add=True,verbose_name="Created at",)
    updated_at = DateTimeField(auto_now=True,verbose_name="Updated at",)

    def __str__(self):
        return f"{str(self.date)} {str(self.price)} "

    

