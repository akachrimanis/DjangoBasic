from django import forms
from .serializers import CustomerSerializer
from .models import Customer



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'active', 'AFM', 'contact_first_name', 'contact_last_name', 'email', 'phone', 'address']
        # Add any other fields that you have in your Customer model

