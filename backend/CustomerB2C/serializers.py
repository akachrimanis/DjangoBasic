
from rest_framework import serializers
from .models import CustomerB2C

class CustomerB2CSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerB2C
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import CustomerUserProfileB2C

class CustomerUserProfileB2CSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUserProfileB2C
        fields = "__all__"
        
        
