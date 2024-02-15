from rest_framework import viewsets
from .models import Dashboardtestdata
from .serializers import DashboardtestdataSerializer
from .forms import DashboardtestdataForm


from rest_framework import generics
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView


def home(request):
    return render(request, "home.html",{})

class DashboardtestdataViewSet(viewsets.ModelViewSet):
    queryset = Dashboardtestdata.objects.all()
    serializer_class = DashboardtestdataSerializer
    
     # Dashboardtestdata Views  
class DashboardtestdataListView(ListView):
    model = Dashboardtestdata
    template_name = 'dashboardtestdata-list.html'
    context_object_name = 'dashboardtestdatas'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all field names excluding 'id'
        fields = [field.verbose_name for field in self.model._meta.get_fields() if field.name != 'id']
        context['fields'] = fields
        return context

    def get_queryset(self):
        # Optionally, you can filter or manipulate the queryset here
        return Dashboardtestdata.objects.all()
    
class DashboardtestdataDetailView(DetailView):
    model = Dashboardtestdata
    template_name = 'dashboardtestdata-details.html'
    context_object_name = 'dashboardtestdatas'

class DashboardtestdataCreateView(CreateView):
    model = Dashboardtestdata
    form_class = DashboardtestdataForm
    template_name = 'dashboardtestdata-form.html'
    success_url = reverse_lazy('dashboardtestdata-list')  # Redirect to the CRUD view after successful creation

class DashboardtestdataUpdateView(UpdateView):
    model = Dashboardtestdata
    form_class = DashboardtestdataForm
    template_name = 'dashboardtestdata-form.html'
    success_url = reverse_lazy('dashboardtestdata-list')  # Redirect to the CRUD view after successful update

class DashboardtestdataDeleteView(DeleteView):
    model = Dashboardtestdata
    template_name = 'dashboardtestdata-confirm-delete.html'
    success_url = reverse_lazy('dashboardtestdata-list')  # Redirect to the CRUD view after successful deletion
   

def Dashboardtestdata_data(request):
    dashboardtestdata_data = Dashboardtestdata.objects.all()
    field_names = [field.verbose_name for field in Dashboardtestdata._meta.fields]
    
    # Print debug information
    print("Field names:", field_names)
    for obj in dashboardtestdata_data:
        print(obj)  # This will print each object and trigger __str__ method

    context = {
        'dashboardtestdata_data': dashboardtestdata_data,
        'field_names': field_names
    }
    
    print(dashboardtestdata_data)
    return render(request, 'dashboardtestdata-list-create.html', context)


class DashboardTemplateBar(TemplateView):
    template_name = "bar.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Dashboardtestdata.objects.all()
        return context
    
class DashboardTemplateLine(TemplateView):
    template_name = "line.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Dashboardtestdata.objects.all()
        return context
    
class DashboardTemplateScatter(TemplateView):
    template_name = "scatter.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Dashboardtestdata.objects.all()
        return context
    
class DashboardTemplateDoughnut(TemplateView):
    template_name = "doughnut.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Dashboardtestdata.objects.all()
        return context

class DashboardTemplateBubble(TemplateView):
    template_name = "bubble.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Dashboardtestdata.objects.all()
        return context
    
    
class DashboardTemplateBubble(TemplateView):
    template_name = "chart_with_date_range.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Dashboardtestdata.objects.all()
        return context
    
class DashboardListViewSearch(ListView):
    model = Dashboardtestdata
    template_name = 'chart-select-field.html'
    context_object_name = 'dashboards'
    paginate_by = 10  # Number of objects per page, you can adjust as needed

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Example: Filtering based on a query parameter in the URL
        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(your_field__icontains=search_query)
        
        # You can add more filtering based on other fields as needed
        
        return queryset
    
    
from django.utils.timezone import make_aware
from datetime import datetime
from django.http import JsonResponse
from django.views.generic import View

class DashboardDataView(View):
    def get(self, request):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        # Convert start_date and end_date strings to datetime objects
        start_date = make_aware(datetime.strptime(start_date, '%Y-%m-%d'))
        end_date = make_aware(datetime.strptime(end_date, '%Y-%m-%d'))

        # Query data based on the date range
        data = Dashboardtestdata.objects.filter(date__range=(start_date, end_date))

        # Prepare data for JSON response
        labels = [obj.date.strftime('%Y-%m-%d') for obj in data]
        values = [obj.price for obj in data]

        return JsonResponse({'labels': labels, 'values': values})