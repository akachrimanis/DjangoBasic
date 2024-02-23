
from rest_framework import serializers
from .models import InteractionType

class InteractionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = InteractionType
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import Interaction

class InteractionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interaction
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import InteractionDetails

class InteractionDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = InteractionDetails
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import TaskType

class TaskTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskType
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"
        
        
