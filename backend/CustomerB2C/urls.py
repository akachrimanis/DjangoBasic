from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .forms import *
from . import views

router = DefaultRouter()
router.register(r'customerb2cs', views.CustomerB2CViewSet)
router.register(r'customeruserprofileb2cs', views.CustomerUserProfileB2CViewSet)
urlpatterns = [




    # customerb2cs
    path('', views.CustomerB2CListView.as_view(), name='customerb2c-list'),
    path('create/', views.CustomerB2CCreateView.as_view(), name='customerb2c-create'),
    path('update/<int:pk>/', views.CustomerB2CUpdateView.as_view(), name='customerb2c-update'),
    path('delete/<int:pk>/', views.CustomerB2CDeleteView.as_view(), name='customerb2c-delete'),
    path('<int:pk>/', views.CustomerB2CListView.as_view(), name='customerb2c-detail'),





    # customeruserprofileb2cs
    path('', views.CustomerUserProfileB2CListView.as_view(), name='customeruserprofileb2c-list'),
    path('create/', views.CustomerUserProfileB2CCreateView.as_view(), name='customeruserprofileb2c-create'),
    path('update/<int:pk>/', views.CustomerUserProfileB2CUpdateView.as_view(), name='customeruserprofileb2c-update'),
    path('delete/<int:pk>/', views.CustomerUserProfileB2CDeleteView.as_view(), name='customeruserprofileb2c-delete'),
    path('<int:pk>/', views.CustomerUserProfileB2CListView.as_view(), name='customeruserprofileb2c-detail'),


    path('api/1/', include(router.urls)),
    path('home/', views.home, name='home'),]
