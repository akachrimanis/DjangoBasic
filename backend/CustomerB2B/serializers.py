
from rest_framework import serializers
from .models import CustomerB2B

class CustomerB2BSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerB2B
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import CustomerB2BGoup

class CustomerB2BGoupSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerB2BGoup
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import CustomerB2BAggregate_country

class CustomerB2BAggregate_countrySerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerB2BAggregate_country
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import CustomerUserProfileB2B

class CustomerUserProfileB2BSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUserProfileB2B
        fields = "__all__"
        
        
