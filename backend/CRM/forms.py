from django import forms
from .serializers import InteractionTypeSerializer
from .models import InteractionType



class InteractionTypeForm(forms.ModelForm):
    class Meta:
        model = InteractionType
        fields = ['name']
        # Add any other fields that you have in your Customer model


from .serializers import InteractionSerializer
from .models import Interaction



class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ['user', 'date', 'interaction_type', 'notes']
        # Add any other fields that you have in your Customer model


from .serializers import InteractionDetailsSerializer
from .models import InteractionDetails



class InteractionDetailsForm(forms.ModelForm):
    class Meta:
        model = InteractionDetails
        fields = ['interaction', 'details', 'handled_by']
        # Add any other fields that you have in your Customer model


from .serializers import TaskTypeSerializer
from .models import TaskType



class TaskTypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = ['name']
        # Add any other fields that you have in your Customer model


from .serializers import TaskSerializer
from .models import Task



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['customer', 'task_type', 'due_date', 'description', 'assigned_to']
        # Add any other fields that you have in your Customer model


