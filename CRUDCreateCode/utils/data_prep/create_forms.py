def create_forms(df, model_name):
    df = df.astype(str)
    
    df = df[df["filter_use"] == "True"]

    form_fields = df[df['forms']=="True"]['Variable'].tolist()
    print(form_fields)
    # Starting script
    forms_content = f"""from django import forms
from .models import {model_name.capitalize()}\n


class {model_name.capitalize()}Form(forms.ModelForm):
    class Meta:
        model = {model_name.capitalize()}
        fields = {form_fields}
        # Add any other fields that you have in your Customer model
"""
    return forms_content




