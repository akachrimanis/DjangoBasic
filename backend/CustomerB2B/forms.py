from django import forms
from .serializers import CustomerB2BSerializer
from .models import CustomerB2B



class CustomerB2BForm(forms.ModelForm):
    class Meta:
        model = CustomerB2B
        fields = ['name', 'email', 'phone', 'website', 'address_line_1', 'address_line_2', 'city', 'state', 'postal_code', 'country', 'contact_person', 'contact_email', 'contact_phone', 'industry', 'company_size', 'annual_revenue', 'tax_id', 'registration_number', 'payment_terms', 'bank_name', 'bank_account_number', 'swift_code', 'company_group', 'notes']
        # Add any other fields that you have in your Customer model


from .serializers import CustomerB2BGoupSerializer
from .models import CustomerB2BGoup



class CustomerB2BGoupForm(forms.ModelForm):
    class Meta:
        model = CustomerB2BGoup
        fields = ['name', 'email', 'phone', 'website', 'address_line_1', 'address_line_2', 'city', 'state', 'postal_code', 'country', 'contact_person', 'contact_email', 'contact_phone', 'industry', 'company_size', 'annual_revenue', 'tax_id', 'registration_number', 'payment_terms', 'bank_name', 'bank_account_number', 'swift_code', 'company_group', 'notes']
        # Add any other fields that you have in your Customer model


from .serializers import CustomerB2BAggregate_countrySerializer
from .models import CustomerB2BAggregate_country



class CustomerB2BAggregate_countryForm(forms.ModelForm):
    class Meta:
        model = CustomerB2BAggregate_country
        fields = ['country ', 'total_customers ', 'total_annual_revenue ', 'total_industries ', 'total_company_size ']
        # Add any other fields that you have in your Customer model


from .serializers import CustomerUserProfileB2BSerializer
from .models import CustomerUserProfileB2B



class CustomerUserProfileB2BForm(forms.ModelForm):
    class Meta:
        model = CustomerUserProfileB2B
        fields = ['company', 'username', 'firstname', 'surname', 'email', 'phone', 'description']
        # Add any other fields that you have in your Customer model


