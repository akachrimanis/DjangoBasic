
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import Individual

class IndividualSerializer(serializers.ModelSerializer):

    class Meta:
        model = Individual
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import Organisation

class OrganisationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organisation
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import Manager

class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manager
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import Employer

class EmployerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employer
        fields = "__all__"
        
        
