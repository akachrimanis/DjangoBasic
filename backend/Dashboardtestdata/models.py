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
    
    class Meta:
        verbose_name = "Dashboard Test Data"
        verbose_name_plural = "Dashboard Test Data"
        ordering = ["-date"]  # Order by date descending by default

    @property
    def price_difference(self):
        """
        Calculate the price difference between this instance and the previous one.
        """
        previous_instance = Dashboardtestdata.objects.filter(date__lt=self.date).order_by('-date').first()
        if previous_instance:
            return self.price - previous_instance.price
        return 0  # Return 0 if there's no previous instance
    
    
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from django.db.models import Count, Sum, Avg, Min, Max
from django.db.models.functions import TruncYear

class DashboardYearlyAggregate(models.Model):
    year = models.IntegerField(unique=True)
    total_price = models.IntegerField(default=0)
    average_price = models.FloatField(default=0)
    min_price = models.IntegerField(default=0)
    max_price = models.IntegerField(default=0)
    num_entries = models.IntegerField(default=0)

    def __str__(self):
        return str(self.year)

@receiver(post_save, sender=Dashboardtestdata)
@receiver(post_delete, sender=Dashboardtestdata)
def update_yearly_aggregates(sender, instance, **kwargs):
    year = instance.date.year
    aggregates = Dashboardtestdata.objects.filter(date__year=year).aggregate(
        total_price=Sum('price'),
        average_price=Avg('price'),
        min_price=Min('price'),
        max_price=Max('price'),
        num_entries=Count('id')
    )
    yearly_aggregate, created = DashboardYearlyAggregate.objects.get_or_create(year=year)
    yearly_aggregate.total_price = aggregates['total_price'] or 0
    yearly_aggregate.average_price = aggregates['average_price'] or 0
    yearly_aggregate.min_price = aggregates['min_price'] or 0
    yearly_aggregate.max_price = aggregates['max_price'] or 0
    yearly_aggregate.num_entries = aggregates['num_entries'] or 0
    yearly_aggregate.save()


