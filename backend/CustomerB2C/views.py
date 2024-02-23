from rest_framework import viewsets
from rest_framework import generics
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

def home(request):
    return render(request, "home.html",{})
from .models import CustomerB2C
from .serializers import CustomerB2CSerializer
from .forms import CustomerB2CForm
from .models import CustomerUserProfileB2C
from .serializers import CustomerUserProfileB2CSerializer
from .forms import CustomerUserProfileB2CForm

class Customerb2cViewSet(viewsets.ModelViewSet):
    queryset = CustomerB2C.objects.all()
    serializer_class = CustomerB2CSerializer
    
     # CustomerB2C Views  
class CustomerB2CListView(ListView):
    model = CustomerB2C
    template_name = 'customerb2c-list.html'
    context_object_name = 'customerb2cs'
    
class CustomerB2CDetailView(DetailView):
    model = CustomerB2C
    template_name = 'customerb2c-details.html'
    context_object_name = 'customerb2cs'

class CustomerB2CCreateView(CreateView):
    model = CustomerB2C
    form_class = CustomerB2CForm
    template_name = 'customerb2c-form.html'
    success_url = reverse_lazy('customerb2c-list')  # Redirect to the CRUD view after successful creation

class CustomerB2CUpdateView(UpdateView):
    model = CustomerB2C
    form_class = CustomerB2CForm
    template_name = 'customerb2c-form.html'
    success_url = reverse_lazy('customerb2c-list')  # Redirect to the CRUD view after successful update

class CustomerB2CDeleteView(DeleteView):
    model = CustomerB2C
    template_name = 'customerb2c-confirm-delete.html'
    success_url = reverse_lazy('customerb2c-list')  # Redirect to the CRUD view after successful deletion
   
    
class Customerb2cViewSet(viewsets.ModelViewSet):
    queryset = CustomerB2C.objects.all()
    serializer_class = CustomerB2CSerializer
    
     # CustomerB2C Views  
class CustomerB2CListView(ListView):
    model = CustomerB2C
    template_name = 'customerb2c-list.html'
    context_object_name = 'customerb2cs'
    
class CustomerB2CDetailView(DetailView):
    model = CustomerB2C
    template_name = 'customerb2c-details.html'
    context_object_name = 'customerb2cs'

class CustomerB2CCreateView(CreateView):
    model = CustomerB2C
    form_class = CustomerB2CForm
    template_name = 'customerb2c-form.html'
    success_url = reverse_lazy('customerb2c-list')  # Redirect to the CRUD view after successful creation

class CustomerB2CUpdateView(UpdateView):
    model = CustomerB2C
    form_class = CustomerB2CForm
    template_name = 'customerb2c-form.html'
    success_url = reverse_lazy('customerb2c-list')  # Redirect to the CRUD view after successful update

class CustomerB2CDeleteView(DeleteView):
    model = CustomerB2C
    template_name = 'customerb2c-confirm-delete.html'
    success_url = reverse_lazy('customerb2c-list')  # Redirect to the CRUD view after successful deletion
   
    
class Customeruserprofileb2cViewSet(viewsets.ModelViewSet):
    queryset = CustomerUserProfileB2C.objects.all()
    serializer_class = CustomerUserProfileB2CSerializer
    
     # CustomerUserProfileB2C Views  
class CustomerUserProfileB2CListView(ListView):
    model = CustomerUserProfileB2C
    template_name = 'customeruserprofileb2c-list.html'
    context_object_name = 'customeruserprofileb2cs'
    
class CustomerUserProfileB2CDetailView(DetailView):
    model = CustomerUserProfileB2C
    template_name = 'customeruserprofileb2c-details.html'
    context_object_name = 'customeruserprofileb2cs'

class CustomerUserProfileB2CCreateView(CreateView):
    model = CustomerUserProfileB2C
    form_class = CustomerUserProfileB2CForm
    template_name = 'customeruserprofileb2c-form.html'
    success_url = reverse_lazy('customeruserprofileb2c-list')  # Redirect to the CRUD view after successful creation

class CustomerUserProfileB2CUpdateView(UpdateView):
    model = CustomerUserProfileB2C
    form_class = CustomerUserProfileB2CForm
    template_name = 'customeruserprofileb2c-form.html'
    success_url = reverse_lazy('customeruserprofileb2c-list')  # Redirect to the CRUD view after successful update

class CustomerUserProfileB2CDeleteView(DeleteView):
    model = CustomerUserProfileB2C
    template_name = 'customeruserprofileb2c-confirm-delete.html'
    success_url = reverse_lazy('customeruserprofileb2c-list')  # Redirect to the CRUD view after successful deletion
   
    
