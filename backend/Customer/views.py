from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
from .forms import CustomerForm


from rest_framework import generics
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


def home(request):
    return render(request, "home.html",{})

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
     # Customer Views  
class CustomerListView(ListView):
    model = Customer
    template_name = 'customer-list.html'
    context_object_name = 'customers'
    
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer-details.html'
    context_object_name = 'customers'

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer-form.html'
    success_url = reverse_lazy('customer-list')  # Redirect to the CRUD view after successful creation

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer-form.html'
    success_url = reverse_lazy('customer-list')  # Redirect to the CRUD view after successful update

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer-confirm-delete.html'
    success_url = reverse_lazy('customer-list')  # Redirect to the CRUD view after successful deletion
   
    
