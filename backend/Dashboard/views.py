from rest_framework import viewsets
from rest_framework import generics
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

def home(request):
    return render(request, "home.html",{})


from .models import Dashboard
from .forms import DashboardForm
from .serializers import DashboardSerializer

class DashboardViewSet(viewsets.ModelViewSet):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
    
     # Dashboard Views  
class DashboardListView(ListView):
    model = Dashboard
    template_name = 'dashboard-list.html'
    context_object_name = 'dashboards'
    
class DashboardDetailView(DetailView):
    model = Dashboard
    template_name = 'dashboard-details.html'
    context_object_name = 'dashboards'

class DashboardCreateView(CreateView):
    model = Dashboard
    form_class = DashboardForm
    template_name = 'dashboard-form.html'
    success_url = reverse_lazy('dashboard-list')  # Redirect to the CRUD view after successful creation

class DashboardUpdateView(UpdateView):
    model = Dashboard
    form_class = DashboardForm
    template_name = 'dashboard-form.html'
    success_url = reverse_lazy('dashboard-list')  # Redirect to the CRUD view after successful update

class DashboardDeleteView(DeleteView):
    model = Dashboard
    template_name = 'dashboard-confirm-delete.html'
    success_url = reverse_lazy('dashboard-list')  # Redirect to the CRUD view after successful deletion
   
    
