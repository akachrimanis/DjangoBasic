from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .forms import *
from . import views


router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet)

urlpatterns = [
    path('api/1/', include(router.urls)),
    path('home/', views.home, name='home'),
    # customers
    path('', views.CustomerListView.as_view(), name='customer-list'),
    path('create/', views.CustomerCreateView.as_view(), name='customer-create'),
    path('update/<int:pk>/', views.CustomerUpdateView.as_view(), name='customer-update'),
    path('delete/<int:pk>/', views.CustomerDeleteView.as_view(), name='customer-delete'),
    path('<int:pk>/', views.CustomerListView.as_view(), name='customer-detail'),


]


# GET /api/1/customers/: List all customers.
# POST /api/1/customers/: Create a new customer.
# GET /api/1/customers/<id>/: Retrieve a customer by ID.
# PUT /api/1/customers/<id>/: Update a customer by ID.
# PATCH /api/1/customers/<id>/: Partially update a customer by ID.
# DELETE /api/1/customers/<id>/: Delete a customer by ID.

