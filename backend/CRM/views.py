from rest_framework import viewsets
from rest_framework import generics
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

def home(request):
    return render(request, "home.html",{})


from .models import InteractionType, Interaction, InteractionDetails, TaskType, Task
from .forms import InteractionTypeForm, InteractionForm, InteractionDetailsForm, TaskTypeForm, TaskForm
from .serializers import InteractionTypeSerializer, InteractionSerializer, InteractionDetailsSerializer, TaskTypeSerializer, TaskSerializer

class InteractionTypeViewSet(viewsets.ModelViewSet):
    queryset = InteractionType.objects.all()
    serializer_class = InteractionTypeSerializer
    
     # InteractionType Views  
class InteractionTypeListView(ListView):
    model = InteractionType
    template_name = 'interactiontype-list.html'
    context_object_name = 'interactiontypes'
    
class InteractionTypeDetailView(DetailView):
    model = InteractionType
    template_name = 'interactiontype-details.html'
    context_object_name = 'interactiontypes'

class InteractionTypeCreateView(CreateView):
    model = InteractionType
    form_class = InteractionTypeForm
    template_name = 'interactiontype-form.html'
    success_url = reverse_lazy('interactiontype-list')  # Redirect to the CRUD view after successful creation

class InteractionTypeUpdateView(UpdateView):
    model = InteractionType
    form_class = InteractionTypeForm
    template_name = 'interactiontype-form.html'
    success_url = reverse_lazy('interactiontype-list')  # Redirect to the CRUD view after successful update

class InteractionTypeDeleteView(DeleteView):
    model = InteractionType
    template_name = 'interactiontype-confirm-delete.html'
    success_url = reverse_lazy('interactiontype-list')  # Redirect to the CRUD view after successful deletion
   
    

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    
     # Interaction Views  
class InteractionListView(ListView):
    model = Interaction
    template_name = 'interaction-list.html'
    context_object_name = 'interactions'
    
class InteractionDetailView(DetailView):
    model = Interaction
    template_name = 'interaction-details.html'
    context_object_name = 'interactions'

class InteractionCreateView(CreateView):
    model = Interaction
    form_class = InteractionForm
    template_name = 'interaction-form.html'
    success_url = reverse_lazy('interaction-list')  # Redirect to the CRUD view after successful creation

class InteractionUpdateView(UpdateView):
    model = Interaction
    form_class = InteractionForm
    template_name = 'interaction-form.html'
    success_url = reverse_lazy('interaction-list')  # Redirect to the CRUD view after successful update

class InteractionDeleteView(DeleteView):
    model = Interaction
    template_name = 'interaction-confirm-delete.html'
    success_url = reverse_lazy('interaction-list')  # Redirect to the CRUD view after successful deletion
   
    

class InteractionDetailsViewSet(viewsets.ModelViewSet):
    queryset = InteractionDetails.objects.all()
    serializer_class = InteractionDetailsSerializer
    
     # InteractionDetails Views  
class InteractionDetailsListView(ListView):
    model = InteractionDetails
    template_name = 'interactiondetails-list.html'
    context_object_name = 'interactiondetailss'
    
class InteractionDetailsDetailView(DetailView):
    model = InteractionDetails
    template_name = 'interactiondetails-details.html'
    context_object_name = 'interactiondetailss'

class InteractionDetailsCreateView(CreateView):
    model = InteractionDetails
    form_class = InteractionDetailsForm
    template_name = 'interactiondetails-form.html'
    success_url = reverse_lazy('interactiondetails-list')  # Redirect to the CRUD view after successful creation

class InteractionDetailsUpdateView(UpdateView):
    model = InteractionDetails
    form_class = InteractionDetailsForm
    template_name = 'interactiondetails-form.html'
    success_url = reverse_lazy('interactiondetails-list')  # Redirect to the CRUD view after successful update

class InteractionDetailsDeleteView(DeleteView):
    model = InteractionDetails
    template_name = 'interactiondetails-confirm-delete.html'
    success_url = reverse_lazy('interactiondetails-list')  # Redirect to the CRUD view after successful deletion
   
    

class TaskTypeViewSet(viewsets.ModelViewSet):
    queryset = TaskType.objects.all()
    serializer_class = TaskTypeSerializer
    
     # TaskType Views  
class TaskTypeListView(ListView):
    model = TaskType
    template_name = 'tasktype-list.html'
    context_object_name = 'tasktypes'
    
class TaskTypeDetailView(DetailView):
    model = TaskType
    template_name = 'tasktype-details.html'
    context_object_name = 'tasktypes'

class TaskTypeCreateView(CreateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = 'tasktype-form.html'
    success_url = reverse_lazy('tasktype-list')  # Redirect to the CRUD view after successful creation

class TaskTypeUpdateView(UpdateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = 'tasktype-form.html'
    success_url = reverse_lazy('tasktype-list')  # Redirect to the CRUD view after successful update

class TaskTypeDeleteView(DeleteView):
    model = TaskType
    template_name = 'tasktype-confirm-delete.html'
    success_url = reverse_lazy('tasktype-list')  # Redirect to the CRUD view after successful deletion
   
    

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
     # Task Views  
class TaskListView(ListView):
    model = Task
    template_name = 'task-list.html'
    context_object_name = 'tasks'
    
class TaskDetailView(DetailView):
    model = Task
    template_name = 'task-details.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task-form.html'
    success_url = reverse_lazy('task-list')  # Redirect to the CRUD view after successful creation

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task-form.html'
    success_url = reverse_lazy('task-list')  # Redirect to the CRUD view after successful update

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task-confirm-delete.html'
    success_url = reverse_lazy('task-list')  # Redirect to the CRUD view after successful deletion
   
    
