from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CustomerB2B, CustomerB2BAggregate_country
from django.db.models import Count, Sum

@receiver(post_save, sender=CustomerB2B)
def update_country_aggregation(sender, instance, **kwargs):
    # Get the country of the customer
    country = instance.country
    
    # Update the CustomerB2BAggregate_country model for the corresponding country
    country_aggregation, _ = CustomerB2BAggregate_country.objects.get_or_create(country=country)

    # Update total customers count
    country_aggregation.total_customers = CustomerB2B.objects.filter(country=country).count()
    
    # Update total annual revenue
    country_aggregation.total_annual_revenue = CustomerB2B.objects.filter(country=country).aggregate(total_revenue=Sum('annual_revenue'))['total_revenue'] or 0

    # Update total industries count
    country_aggregation.total_industries = CustomerB2B.objects.filter(country=country).values('industry').distinct().count()

    # Update total company size
    country_aggregation.total_company_size = CustomerB2B.objects.filter(country=country).aggregate(total_company_size=Sum('company_size'))['total_company_size'] or 0
    
    # Save the changes
    country_aggregation.save()

@receiver(post_delete, sender=CustomerB2B)
def delete_country_aggregation(sender, instance, **kwargs):
    # Get the country of the customer
    country = instance.country

    # Update the CustomerB2BAggregate_country model for the corresponding country
    country_aggregation, _ = CustomerB2BAggregate_country.objects.get_or_create(country=country)

    # Update total customers count
    country_aggregation.total_customers = CustomerB2B.objects.filter(country=country).count()

    # Update total annual revenue
    country_aggregation.total_annual_revenue = CustomerB2B.objects.filter(country=country).aggregate(total_revenue=Sum('annual_revenue'))['total_revenue'] or 0

    # Update total industries count
    country_aggregation.total_industries = CustomerB2B.objects.filter(country=country).values('industry').distinct().count()

    # Update total company size
    country_aggregation.total_company_size = CustomerB2B.objects.filter(country=country).aggregate(total_company_size=Sum('company_size'))['total_company_size'] or 0

    # Save the changes
    country_aggregation.save()