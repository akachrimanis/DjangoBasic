from rest_framework import viewsets
from rest_framework import generics
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

def home(request):
    return render(request, "home.html",{})


from .models import Employee, Individual, Organization, Manager, Employer
from .forms import EmployeeForm, IndividualForm, OrganizationForm, ManagerForm, EmployerForm
from .serializers import EmployeeSerializer, IndividualSerializer, OrganizationSerializer, ManagerSerializer, EmployerSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
     # Employee Views  
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee-list.html'
    context_object_name = 'employees'
    
class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee-details.html'
    context_object_name = 'employees'

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee-form.html'
    success_url = reverse_lazy('employee-list')  # Redirect to the CRUD view after successful creation

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee-form.html'
    success_url = reverse_lazy('employee-list')  # Redirect to the CRUD view after successful update

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee-confirm-delete.html'
    success_url = reverse_lazy('employee-list')  # Redirect to the CRUD view after successful deletion
   
    

class IndividualViewSet(viewsets.ModelViewSet):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer
    
     # Individual Views  
class IndividualListView(ListView):
    model = Individual
    template_name = 'individual-list.html'
    context_object_name = 'individuals'
    
class IndividualDetailView(DetailView):
    model = Individual
    template_name = 'individual-details.html'
    context_object_name = 'individuals'

class IndividualCreateView(CreateView):
    model = Individual
    form_class = IndividualForm
    template_name = 'individual-form.html'
    success_url = reverse_lazy('individual-list')  # Redirect to the CRUD view after successful creation

class IndividualUpdateView(UpdateView):
    model = Individual
    form_class = IndividualForm
    template_name = 'individual-form.html'
    success_url = reverse_lazy('individual-list')  # Redirect to the CRUD view after successful update

class IndividualDeleteView(DeleteView):
    model = Individual
    template_name = 'individual-confirm-delete.html'
    success_url = reverse_lazy('individual-list')  # Redirect to the CRUD view after successful deletion
   
    

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    
     # Organization Views  
class OrganizationListView(ListView):
    model = Organization
    template_name = 'organization-list.html'
    context_object_name = 'organizations'
    
class OrganizationDetailView(DetailView):
    model = Organization
    template_name = 'organization-details.html'
    context_object_name = 'organizations'

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'organization-form.html'
    success_url = reverse_lazy('organization-list')  # Redirect to the CRUD view after successful creation

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'organization-form.html'
    success_url = reverse_lazy('organization-list')  # Redirect to the CRUD view after successful update

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'organization-confirm-delete.html'
    success_url = reverse_lazy('organization-list')  # Redirect to the CRUD view after successful deletion
   
    

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    
     # Manager Views  
class ManagerListView(ListView):
    model = Manager
    template_name = 'manager-list.html'
    context_object_name = 'managers'
    
class ManagerDetailView(DetailView):
    model = Manager
    template_name = 'manager-details.html'
    context_object_name = 'managers'

class ManagerCreateView(CreateView):
    model = Manager
    form_class = ManagerForm
    template_name = 'manager-form.html'
    success_url = reverse_lazy('manager-list')  # Redirect to the CRUD view after successful creation

class ManagerUpdateView(UpdateView):
    model = Manager
    form_class = ManagerForm
    template_name = 'manager-form.html'
    success_url = reverse_lazy('manager-list')  # Redirect to the CRUD view after successful update

class ManagerDeleteView(DeleteView):
    model = Manager
    template_name = 'manager-confirm-delete.html'
    success_url = reverse_lazy('manager-list')  # Redirect to the CRUD view after successful deletion
   
    

class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    
     # Employer Views  
class EmployerListView(ListView):
    model = Employer
    template_name = 'employer-list.html'
    context_object_name = 'employers'
    
class EmployerDetailView(DetailView):
    model = Employer
    template_name = 'employer-details.html'
    context_object_name = 'employers'

class EmployerCreateView(CreateView):
    model = Employer
    form_class = EmployerForm
    template_name = 'employer-form.html'
    success_url = reverse_lazy('employer-list')  # Redirect to the CRUD view after successful creation

class EmployerUpdateView(UpdateView):
    model = Employer
    form_class = EmployerForm
    template_name = 'employer-form.html'
    success_url = reverse_lazy('employer-list')  # Redirect to the CRUD view after successful update

class EmployerDeleteView(DeleteView):
    model = Employer
    template_name = 'employer-confirm-delete.html'
    success_url = reverse_lazy('employer-list')  # Redirect to the CRUD view after successful deletion
   
    
