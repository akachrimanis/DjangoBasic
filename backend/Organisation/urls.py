from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .forms import *
from . import views

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)
router.register(r'individuals', views.IndividualViewSet)
router.register(r'organisations', views.OrganisationViewSet)
router.register(r'managers', views.ManagerViewSet)
router.register(r'employers', views.EmployerViewSet)
urlpatterns = [




    # employees
    path('', views.EmployeeListView.as_view(), name='employee-list'),
    path('create/', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='employee-delete'),
    path('<int:pk>/', views.EmployeeListView.as_view(), name='employee-detail'),





    # individuals
    path('', views.IndividualListView.as_view(), name='individual-list'),
    path('create/', views.IndividualCreateView.as_view(), name='individual-create'),
    path('update/<int:pk>/', views.IndividualUpdateView.as_view(), name='individual-update'),
    path('delete/<int:pk>/', views.IndividualDeleteView.as_view(), name='individual-delete'),
    path('<int:pk>/', views.IndividualListView.as_view(), name='individual-detail'),





    # Organisations
    path('', views.OrganisationListView.as_view(), name='Organisation-list'),
    path('create/', views.OrganisationCreateView.as_view(), name='Organisation-create'),
    path('update/<int:pk>/', views.OrganisationUpdateView.as_view(), name='Organisation-update'),
    path('delete/<int:pk>/', views.OrganisationDeleteView.as_view(), name='Organisation-delete'),
    path('<int:pk>/', views.OrganisationListView.as_view(), name='Organisation-detail'),





    # managers
    path('', views.ManagerListView.as_view(), name='manager-list'),
    path('create/', views.ManagerCreateView.as_view(), name='manager-create'),
    path('update/<int:pk>/', views.ManagerUpdateView.as_view(), name='manager-update'),
    path('delete/<int:pk>/', views.ManagerDeleteView.as_view(), name='manager-delete'),
    path('<int:pk>/', views.ManagerListView.as_view(), name='manager-detail'),





    # employers
    path('', views.EmployerListView.as_view(), name='employer-list'),
    path('create/', views.EmployerCreateView.as_view(), name='employer-create'),
    path('update/<int:pk>/', views.EmployerUpdateView.as_view(), name='employer-update'),
    path('delete/<int:pk>/', views.EmployerDeleteView.as_view(), name='employer-delete'),
    path('<int:pk>/', views.EmployerListView.as_view(), name='employer-detail'),


    path('api/1/', include(router.urls)),
    path('home/', views.home, name='home'),]
