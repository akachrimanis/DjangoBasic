from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .forms import *
from . import views

router = DefaultRouter()
router.register(r'dashboards', views.DashboardViewSet)
urlpatterns = [




    # dashboards
    path('', views.DashboardListView.as_view(), name='dashboard-list'),
    path('create/', views.DashboardCreateView.as_view(), name='dashboard-create'),
    path('update/<int:pk>/', views.DashboardUpdateView.as_view(), name='dashboard-update'),
    path('delete/<int:pk>/', views.DashboardDeleteView.as_view(), name='dashboard-delete'),
    path('<int:pk>/', views.DashboardListView.as_view(), name='dashboard-detail'),


    path('api/1/', include(router.urls)),
    path('home/', views.home, name='home'),]
