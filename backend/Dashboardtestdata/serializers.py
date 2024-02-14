from rest_framework import serializers
from .models import Dashboardtestdata

class DashboardtestdataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dashboardtestdata
        fields = "__all__"
        
