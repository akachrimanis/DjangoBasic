# custom_filters.py

from django import template

register = template.Library()

@register.filter(name="get_fields")
def get_fields(obj):
    return obj._meta.fields