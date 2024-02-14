# custom_tags.py

from django import template
from django.db.models import Model

register = template.Library()

@register.simple_tag
def get_model_fields(model):
    if isinstance(model, Model):
        return model._meta.get_fields()
    else:
        return None