from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .forms import *
from . import views

router = DefaultRouter()
router.register(r'customerb2bs', views.CustomerB2BViewSet)
router.register(r'customerb2bgoups', views.CustomerB2BGoupViewSet)
router.register(r'customerb2baggregate_countrys', views.CustomerB2BAggregate_countryViewSet)
router.register(r'customeruserprofileb2bs', views.CustomerUserProfileB2BViewSet)
urlpatterns = [




    # customerb2bs
    path('CustomerB2B/', views.CustomerB2BListView.as_view(), name='customerb2b-list'),
    path('CustomerB2B/list', views.CustomerB2BListView.as_view(), name='customerb2b-list2'),

    path('CustomerB2B/create/', views.CustomerB2BCreateView.as_view(), name='customerb2b-create'),
    path('CustomerB2B/update/<int:pk>/', views.CustomerB2BUpdateView.as_view(), name='customerb2b-update'),
    path('CustomerB2B/delete/<int:pk>/', views.CustomerB2BDeleteView.as_view(), name='customerb2b-delete'),
    path('CustomerB2B/<int:pk>/', views.CustomerB2BListView.as_view(), name='customerb2b-detail'),





    # customerb2bgoups
    path('CustomerB2BGoup/', views.CustomerB2BGoupListView.as_view(), name='customerb2bgoup-list'),
    path('CustomerB2BGoup/create/', views.CustomerB2BGoupCreateView.as_view(), name='customerb2bgoup-create'),
    path('CustomerB2BGoup/update/<int:pk>/', views.CustomerB2BGoupUpdateView.as_view(), name='customerb2bgoup-update'),
    path('CustomerB2BGoup/delete/<int:pk>/', views.CustomerB2BGoupDeleteView.as_view(), name='customerb2bgoup-delete'),
    path('CustomerB2BGoup/<int:pk>/', views.CustomerB2BGoupListView.as_view(), name='customerb2bgoup-detail'),





    # customerb2baggregate_countrys
    path('CustomerB2BAggregate_country/', views.CustomerB2BAggregate_countryListView.as_view(), name='customerb2baggregate_country-list'),
    path('CustomerB2BAggregate_country/create/', views.CustomerB2BAggregate_countryCreateView.as_view(), name='customerb2baggregate_country-create'),
    path('CustomerB2BAggregate_country/update/<int:pk>/', views.CustomerB2BAggregate_countryUpdateView.as_view(), name='customerb2baggregate_country-update'),
    path('CustomerB2BAggregate_country/delete/<int:pk>/', views.CustomerB2BAggregate_countryDeleteView.as_view(), name='customerb2baggregate_country-delete'),
    path('CustomerB2BAggregate_country/<int:pk>/', views.CustomerB2BAggregate_countryListView.as_view(), name='customerb2baggregate_country-detail'),





    # customeruserprofileb2bs
    path('CustomerUserProfileB2B/', views.CustomerUserProfileB2BListView.as_view(), name='customeruserprofileb2b-list'),
    path('CustomerUserProfileB2B/create/', views.CustomerUserProfileB2BCreateView.as_view(), name='customeruserprofileb2b-create'),
    path('CustomerUserProfileB2B/update/<int:pk>/', views.CustomerUserProfileB2BUpdateView.as_view(), name='customeruserprofileb2b-update'),
    path('CustomerUserProfileB2B/delete/<int:pk>/', views.CustomerUserProfileB2BDeleteView.as_view(), name='customeruserprofileb2b-delete'),
    path('CustomerUserProfileB2B/<int:pk>/', views.CustomerUserProfileB2BListView.as_view(), name='customeruserprofileb2b-detail'),


    path('api/1/', include(router.urls)),
    path('home/', views.home, name='home'),]
