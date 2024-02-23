from django import forms
from .serializers import DashboardSerializer
from .models import Dashboard



class DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ['date', 'price']
        # Add any other fields that you have in your Customer model


