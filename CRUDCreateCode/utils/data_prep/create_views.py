def create_views(df, model_name):
    df = df.astype(str)

    # Starting script
    views_content = f"""from rest_framework import viewsets
from .models import {model_name.capitalize()}
from .serializers import {model_name.capitalize()}Serializer
from .forms import {model_name.capitalize()}Form\n

from rest_framework import generics
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


def home(request):
    return render(request, "home.html",{{}})
"""
    
    views_class = f"""\nclass {model_name.capitalize()}ViewSet(viewsets.ModelViewSet):
    queryset = {model_name.capitalize()}.objects.all()
    serializer_class = {model_name.capitalize()}Serializer
    
     # {model_name} Views  
class {model_name}ListView(ListView):
    model = {model_name}
    template_name = '{model_name.lower()}-list.html'
    context_object_name = '{model_name.lower()}s'
    
class {model_name}DetailView(DetailView):
    model = {model_name}
    template_name = '{model_name.lower()}-details.html'
    context_object_name = '{model_name.lower()}s'

class {model_name}CreateView(CreateView):
    model = {model_name}
    form_class = {model_name}Form
    template_name = '{model_name.lower()}-form.html'
    success_url = reverse_lazy('{model_name.lower()}-list')  # Redirect to the CRUD view after successful creation

class {model_name}UpdateView(UpdateView):
    model = {model_name}
    form_class = {model_name}Form
    template_name = '{model_name.lower()}-form.html'
    success_url = reverse_lazy('{model_name.lower()}-list')  # Redirect to the CRUD view after successful update

class {model_name}DeleteView(DeleteView):
    model = {model_name}
    template_name = '{model_name.lower()}-confirm-delete.html'
    success_url = reverse_lazy('{model_name.lower()}-list')  # Redirect to the CRUD view after successful deletion
   
    """
    print(views_content + views_class)
    return views_content + views_class

