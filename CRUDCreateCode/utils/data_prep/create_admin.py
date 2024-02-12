def create_admin(df, model_name):
    admin_context = f"""from django.contrib import admin
from .models import {model_name}
admin.site.register({model_name})"""
    return admin_context
