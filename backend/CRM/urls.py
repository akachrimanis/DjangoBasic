from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .forms import *
from . import views

router = DefaultRouter()
router.register(r'interactiontypes', views.InteractionTypeViewSet)
router.register(r'interactions', views.InteractionViewSet)
router.register(r'interactiondetailss', views.InteractionDetailsViewSet)
router.register(r'tasktypes', views.TaskTypeViewSet)
router.register(r'tasks', views.TaskViewSet)
urlpatterns = [




    # interactiontypes
    path('', views.InteractionTypeListView.as_view(), name='interactiontype-list'),
    path('create/', views.InteractionTypeCreateView.as_view(), name='interactiontype-create'),
    path('update/<int:pk>/', views.InteractionTypeUpdateView.as_view(), name='interactiontype-update'),
    path('delete/<int:pk>/', views.InteractionTypeDeleteView.as_view(), name='interactiontype-delete'),
    path('<int:pk>/', views.InteractionTypeListView.as_view(), name='interactiontype-detail'),





    # interactions
    path('', views.InteractionListView.as_view(), name='interaction-list'),
    path('create/', views.InteractionCreateView.as_view(), name='interaction-create'),
    path('update/<int:pk>/', views.InteractionUpdateView.as_view(), name='interaction-update'),
    path('delete/<int:pk>/', views.InteractionDeleteView.as_view(), name='interaction-delete'),
    path('<int:pk>/', views.InteractionListView.as_view(), name='interaction-detail'),





    # interactiondetailss
    path('', views.InteractionDetailsListView.as_view(), name='interactiondetails-list'),
    path('create/', views.InteractionDetailsCreateView.as_view(), name='interactiondetails-create'),
    path('update/<int:pk>/', views.InteractionDetailsUpdateView.as_view(), name='interactiondetails-update'),
    path('delete/<int:pk>/', views.InteractionDetailsDeleteView.as_view(), name='interactiondetails-delete'),
    path('<int:pk>/', views.InteractionDetailsListView.as_view(), name='interactiondetails-detail'),





    # tasktypes
    path('', views.TaskTypeListView.as_view(), name='tasktype-list'),
    path('create/', views.TaskTypeCreateView.as_view(), name='tasktype-create'),
    path('update/<int:pk>/', views.TaskTypeUpdateView.as_view(), name='tasktype-update'),
    path('delete/<int:pk>/', views.TaskTypeDeleteView.as_view(), name='tasktype-delete'),
    path('<int:pk>/', views.TaskTypeListView.as_view(), name='tasktype-detail'),





    # tasks
    path('', views.TaskListView.as_view(), name='task-list'),
    path('create/', views.TaskCreateView.as_view(), name='task-create'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('<int:pk>/', views.TaskListView.as_view(), name='task-detail'),


    path('api/1/', include(router.urls)),
    path('home/', views.home, name='home'),]
