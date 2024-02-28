from django import forms
from .serializers import CustomerB2CSerializer
from .models import CustomerB2C



class CustomerB2CForm(forms.ModelForm):
    class Meta:
        model = CustomerB2C
        fields = ['firstname', 'surname', 'date_of_birth', 'email', 'phone', 'website', 'address_line_1', 'address_line_2', 'city', 'state', 'postal_code', 'country', 'notes']
        # Add any other fields that you have in your Customer model


from .serializers import CustomerUserProfileB2CSerializer
from .models import CustomerUserProfileB2C



class CustomerUserProfileB2CForm(forms.ModelForm):
    class Meta:
        model = CustomerUserProfileB2C
        fields = ['firstname', 'surname', 'email', 'phone']
        # Add any other fields that you have in your Customer model


