def create_urls(df, model_name):
    df = df.astype(str)

    # Starting script
    urls_content = f"""from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .forms import *
from . import views\n

router = DefaultRouter()
router.register(r'{model_name.lower()}s', views.{model_name.capitalize()}ViewSet)

urlpatterns = [
    path('api/1/', include(router.urls)),
    path('home/', views.home, name='home'),
    # {model_name.lower()}s
    path('', views.{model_name}ListView.as_view(), name='{model_name.lower()}-list'),
    path('create/', views.{model_name}CreateView.as_view(), name='{model_name.lower()}-create'),
    path('update/<int:pk>/', views.{model_name}UpdateView.as_view(), name='{model_name.lower()}-update'),
    path('delete/<int:pk>/', views.{model_name}DeleteView.as_view(), name='{model_name.lower()}-delete'),
    path('<int:pk>/', views.{model_name}ListView.as_view(), name='{model_name.lower()}-detail'),


]


# GET /api/1/customers/: List all customers.
# POST /api/1/customers/: Create a new customer.
# GET /api/1/customers/<id>/: Retrieve a customer by ID.
# PUT /api/1/customers/<id>/: Update a customer by ID.
# PATCH /api/1/customers/<id>/: Partially update a customer by ID.
# DELETE /api/1/customers/<id>/: Delete a customer by ID.
"""
    return urls_content