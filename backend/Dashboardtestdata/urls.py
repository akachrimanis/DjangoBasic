from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .forms import *
from . import views


router = DefaultRouter()
router.register(r'dashboardtestdatas', views.DashboardtestdataViewSet)

urlpatterns = [
    path('api/1/', include(router.urls)),
    path('home/', views.home, name='home'),
    # dashboardtestdatas
    path('', views.DashboardtestdataListView.as_view(), name='dashboardtestdata-list'),
    path('create/', views.DashboardtestdataCreateView.as_view(), name='dashboardtestdata-create'),
    path('update/<int:pk>/', views.DashboardtestdataUpdateView.as_view(), name='dashboardtestdata-update'),
    path('delete/<int:pk>/', views.DashboardtestdataDeleteView.as_view(), name='dashboardtestdata-delete'),
    path('<int:pk>/', views.DashboardtestdataListView.as_view(), name='dashboardtestdata-detail'),
    path('api/2/', views.DashboardtestdataViewSet.as_view({'get': 'list', 'post': 'create'}), name='dashboardtestdata-list'),
    path('api/2/<int:pk>/', views.DashboardtestdataViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='dashboardtestdata-detail'),
    path('data-list/', views.Dashboardtestdata_data, name='dashboardtestdata-list-create'),
    path('bar/', views.DashboardTemplateBar.as_view(), name='bar'),
    path('line/', views.DashboardTemplateLine.as_view(), name='line'),
    path('scatter/', views.DashboardTemplateScatter.as_view(), name='scatter'),
    path('bubble/', views.DashboardTemplateBubble.as_view(), name='bubble'),
    path('doughnut/', views.DashboardTemplateDoughnut.as_view(), name='doughnut'),
    path('chart_with_date_range/', views.DashboardTemplateDoughnut.as_view(), name='chart_with_date_range'),
    path('doughnut/', views.DashboardTemplateDoughnut.as_view(), name='doughnut'),



]


# GET /api/1/customers/: List all customers.
# POST /api/1/customers/: Create a new customer.
# GET /api/1/customers/<id>/: Retrieve a customer by ID.
# PUT /api/1/customers/<id>/: Update a customer by ID.
# PATCH /api/1/customers/<id>/: Partially update a customer by ID.
# DELETE /api/1/customers/<id>/: Delete a customer by ID.

