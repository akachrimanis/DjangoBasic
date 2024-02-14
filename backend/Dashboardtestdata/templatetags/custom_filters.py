from django import template

register = template.Library()

@register.filter
def get_attribute(obj, attr_name):
    """Custom template filter to get attribute value of an object."""
    return getattr(obj, attr_name, None)