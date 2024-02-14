from django import forms
from .serializers import DashboardtestdataSerializer
from .models import Dashboardtestdata



class DashboardtestdataForm(forms.ModelForm):
    class Meta:
        model = Dashboardtestdata
        fields = ['date', 'price']
        # Add any other fields that you have in your Customer model

