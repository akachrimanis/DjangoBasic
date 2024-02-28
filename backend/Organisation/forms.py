from django import forms
from .serializers import EmployeeSerializer
from .models import Employee



class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'surname', 'age', 'email', 'phone', 'address', 'department', 'role', 'employer', 'manager', 'organization']
        # Add any other fields that you have in your Customer model


from .serializers import IndividualSerializer
from .models import Individual



class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ['user', 'employee',]
        # Add any other fields that you have in your Customer model


from .serializers import OrganisationSerializer
from .models import Organisation



class OrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ['name', 'address']
        # Add any other fields that you have in your Customer model


from .serializers import ManagerSerializer
from .models import Manager



class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['first_name', 'surname', 'age', 'email', 'phone', 'address', 'department', 'role', 'employer', 'organization']
        # Add any other fields that you have in your Customer model


from .serializers import EmployerSerializer
from .models import Employer



class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['name', 'email', 'password', 'company_name', 'organization']
        # Add any other fields that you have in your Customer model


