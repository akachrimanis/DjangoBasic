from rest_framework import viewsets
from rest_framework import generics
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

def home(request):
    return render(request, "home.html",{})


from .models import CustomerB2B, CustomerB2BGoup, CustomerB2BAggregate_country, CustomerUserProfileB2B
from .forms import CustomerB2BForm, CustomerB2BGoupForm, CustomerB2BAggregate_countryForm, CustomerUserProfileB2BForm
from .serializers import CustomerB2BSerializer, CustomerB2BGoupSerializer, CustomerB2BAggregate_countrySerializer, CustomerUserProfileB2BSerializer

class CustomerB2BViewSet(viewsets.ModelViewSet):
    queryset = CustomerB2B.objects.all()
    serializer_class = CustomerB2BSerializer
    
     # CustomerB2B Views  
class CustomerB2BListView(ListView):
    model = CustomerB2B
    template_name = 'customerb2b-list.html'
    context_object_name = 'customerb2bs'
    
class CustomerB2BDetailView(DetailView):
    model = CustomerB2B
    template_name = 'customerb2b-details.html'
    context_object_name = 'customerb2bs'

class CustomerB2BCreateView(CreateView):
    model = CustomerB2B
    form_class = CustomerB2BForm
    template_name = 'customerb2b-form.html'
    success_url = reverse_lazy('customerb2b-list')  # Redirect to the CRUD view after successful creation

class CustomerB2BUpdateView(UpdateView):
    model = CustomerB2B
    form_class = CustomerB2BForm
    template_name = 'customerb2b-form.html'
    success_url = reverse_lazy('customerb2b-list')  # Redirect to the CRUD view after successful update

class CustomerB2BDeleteView(DeleteView):
    model = CustomerB2B
    template_name = 'customerb2b-confirm-delete.html'
    success_url = reverse_lazy('customerb2b-list')  # Redirect to the CRUD view after successful deletion
   
    

class CustomerB2BGoupViewSet(viewsets.ModelViewSet):
    queryset = CustomerB2BGoup.objects.all()
    serializer_class = CustomerB2BGoupSerializer
    
     # CustomerB2BGoup Views  
class CustomerB2BGoupListView(ListView):
    model = CustomerB2BGoup
    template_name = 'customerb2bgoup-list.html'
    context_object_name = 'customerb2bgoups'
    
class CustomerB2BGoupDetailView(DetailView):
    model = CustomerB2BGoup
    template_name = 'customerb2bgoup-details.html'
    context_object_name = 'customerb2bgoups'

class CustomerB2BGoupCreateView(CreateView):
    model = CustomerB2BGoup
    form_class = CustomerB2BGoupForm
    template_name = 'customerb2bgoup-form.html'
    success_url = reverse_lazy('customerb2bgoup-list')  # Redirect to the CRUD view after successful creation

class CustomerB2BGoupUpdateView(UpdateView):
    model = CustomerB2BGoup
    form_class = CustomerB2BGoupForm
    template_name = 'customerb2bgoup-form.html'
    success_url = reverse_lazy('customerb2bgoup-list')  # Redirect to the CRUD view after successful update

class CustomerB2BGoupDeleteView(DeleteView):
    model = CustomerB2BGoup
    template_name = 'customerb2bgoup-confirm-delete.html'
    success_url = reverse_lazy('customerb2bgoup-list')  # Redirect to the CRUD view after successful deletion
   
    

class CustomerB2BAggregate_countryViewSet(viewsets.ModelViewSet):
    queryset = CustomerB2BAggregate_country.objects.all()
    serializer_class = CustomerB2BAggregate_countrySerializer
    
     # CustomerB2BAggregate_country Views  
class CustomerB2BAggregate_countryListView(ListView):
    model = CustomerB2BAggregate_country
    template_name = 'customerb2baggregate_country-list.html'
    context_object_name = 'customerb2baggregate_countrys'
    
class CustomerB2BAggregate_countryDetailView(DetailView):
    model = CustomerB2BAggregate_country
    template_name = 'customerb2baggregate_country-details.html'
    context_object_name = 'customerb2baggregate_countrys'

class CustomerB2BAggregate_countryCreateView(CreateView):
    model = CustomerB2BAggregate_country
    form_class = CustomerB2BAggregate_countryForm
    template_name = 'customerb2baggregate_country-form.html'
    success_url = reverse_lazy('customerb2baggregate_country-list')  # Redirect to the CRUD view after successful creation

class CustomerB2BAggregate_countryUpdateView(UpdateView):
    model = CustomerB2BAggregate_country
    form_class = CustomerB2BAggregate_countryForm
    template_name = 'customerb2baggregate_country-form.html'
    success_url = reverse_lazy('customerb2baggregate_country-list')  # Redirect to the CRUD view after successful update

class CustomerB2BAggregate_countryDeleteView(DeleteView):
    model = CustomerB2BAggregate_country
    template_name = 'customerb2baggregate_country-confirm-delete.html'
    success_url = reverse_lazy('customerb2baggregate_country-list')  # Redirect to the CRUD view after successful deletion
   
    

class CustomerUserProfileB2BViewSet(viewsets.ModelViewSet):
    queryset = CustomerUserProfileB2B.objects.all()
    serializer_class = CustomerUserProfileB2BSerializer
    
     # CustomerUserProfileB2B Views  
class CustomerUserProfileB2BListView(ListView):
    model = CustomerUserProfileB2B
    template_name = 'customeruserprofileb2b-list.html'
    context_object_name = 'customeruserprofileb2bs'
    
class CustomerUserProfileB2BDetailView(DetailView):
    model = CustomerUserProfileB2B
    template_name = 'customeruserprofileb2b-details.html'
    context_object_name = 'customeruserprofileb2bs'

class CustomerUserProfileB2BCreateView(CreateView):
    model = CustomerUserProfileB2B
    form_class = CustomerUserProfileB2BForm
    template_name = 'customeruserprofileb2b-form.html'
    success_url = reverse_lazy('customeruserprofileb2b-list')  # Redirect to the CRUD view after successful creation

class CustomerUserProfileB2BUpdateView(UpdateView):
    model = CustomerUserProfileB2B
    form_class = CustomerUserProfileB2BForm
    template_name = 'customeruserprofileb2b-form.html'
    success_url = reverse_lazy('customeruserprofileb2b-list')  # Redirect to the CRUD view after successful update

class CustomerUserProfileB2BDeleteView(DeleteView):
    model = CustomerUserProfileB2B
    template_name = 'customeruserprofileb2b-confirm-delete.html'
    success_url = reverse_lazy('customeruserprofileb2b-list')  # Redirect to the CRUD view after successful deletion
   
    
