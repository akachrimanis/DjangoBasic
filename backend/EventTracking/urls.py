from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .forms import *
from . import views

router = DefaultRouter()
router.register(r'usersessions', views.UserSessionViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'userdevices', views.UserDeviceViewSet)
router.register(r'pageviews', views.PageViewViewSet)
router.register(r'clickevents', views.ClickEventViewSet)
router.register(r'searchquerys', views.SearchQueryViewSet)
router.register(r'userpreferences', views.UserPreferenceViewSet)
router.register(r'cartactivitys', views.CartActivityViewSet)
router.register(r'wishlists', views.WishlistViewSet)
router.register(r'userfeedbacks', views.UserFeedbackViewSet)
router.register(r'errorlogs', views.ErrorLogViewSet)
urlpatterns = [




    # usersessions
    path('', views.UserSessionListView.as_view(), name='usersession-list'),
    path('create/', views.UserSessionCreateView.as_view(), name='usersession-create'),
    path('update/<int:pk>/', views.UserSessionUpdateView.as_view(), name='usersession-update'),
    path('delete/<int:pk>/', views.UserSessionDeleteView.as_view(), name='usersession-delete'),
    path('<int:pk>/', views.UserSessionListView.as_view(), name='usersession-detail'),





    # events
    path('', views.EventListView.as_view(), name='event-list'),
    path('create/', views.EventCreateView.as_view(), name='event-create'),
    path('update/<int:pk>/', views.EventUpdateView.as_view(), name='event-update'),
    path('delete/<int:pk>/', views.EventDeleteView.as_view(), name='event-delete'),
    path('<int:pk>/', views.EventListView.as_view(), name='event-detail'),





    # userdevices
    path('', views.UserDeviceListView.as_view(), name='userdevice-list'),
    path('create/', views.UserDeviceCreateView.as_view(), name='userdevice-create'),
    path('update/<int:pk>/', views.UserDeviceUpdateView.as_view(), name='userdevice-update'),
    path('delete/<int:pk>/', views.UserDeviceDeleteView.as_view(), name='userdevice-delete'),
    path('<int:pk>/', views.UserDeviceListView.as_view(), name='userdevice-detail'),





    # pageviews
    path('', views.PageViewListView.as_view(), name='pageview-list'),
    path('create/', views.PageViewCreateView.as_view(), name='pageview-create'),
    path('update/<int:pk>/', views.PageViewUpdateView.as_view(), name='pageview-update'),
    path('delete/<int:pk>/', views.PageViewDeleteView.as_view(), name='pageview-delete'),
    path('<int:pk>/', views.PageViewListView.as_view(), name='pageview-detail'),





    # clickevents
    path('', views.ClickEventListView.as_view(), name='clickevent-list'),
    path('create/', views.ClickEventCreateView.as_view(), name='clickevent-create'),
    path('update/<int:pk>/', views.ClickEventUpdateView.as_view(), name='clickevent-update'),
    path('delete/<int:pk>/', views.ClickEventDeleteView.as_view(), name='clickevent-delete'),
    path('<int:pk>/', views.ClickEventListView.as_view(), name='clickevent-detail'),





    # searchquerys
    path('', views.SearchQueryListView.as_view(), name='searchquery-list'),
    path('create/', views.SearchQueryCreateView.as_view(), name='searchquery-create'),
    path('update/<int:pk>/', views.SearchQueryUpdateView.as_view(), name='searchquery-update'),
    path('delete/<int:pk>/', views.SearchQueryDeleteView.as_view(), name='searchquery-delete'),
    path('<int:pk>/', views.SearchQueryListView.as_view(), name='searchquery-detail'),





    # userpreferences
    path('', views.UserPreferenceListView.as_view(), name='userpreference-list'),
    path('create/', views.UserPreferenceCreateView.as_view(), name='userpreference-create'),
    path('update/<int:pk>/', views.UserPreferenceUpdateView.as_view(), name='userpreference-update'),
    path('delete/<int:pk>/', views.UserPreferenceDeleteView.as_view(), name='userpreference-delete'),
    path('<int:pk>/', views.UserPreferenceListView.as_view(), name='userpreference-detail'),





    # cartactivitys
    path('', views.CartActivityListView.as_view(), name='cartactivity-list'),
    path('create/', views.CartActivityCreateView.as_view(), name='cartactivity-create'),
    path('update/<int:pk>/', views.CartActivityUpdateView.as_view(), name='cartactivity-update'),
    path('delete/<int:pk>/', views.CartActivityDeleteView.as_view(), name='cartactivity-delete'),
    path('<int:pk>/', views.CartActivityListView.as_view(), name='cartactivity-detail'),





    # wishlists
    path('', views.WishlistListView.as_view(), name='wishlist-list'),
    path('create/', views.WishlistCreateView.as_view(), name='wishlist-create'),
    path('update/<int:pk>/', views.WishlistUpdateView.as_view(), name='wishlist-update'),
    path('delete/<int:pk>/', views.WishlistDeleteView.as_view(), name='wishlist-delete'),
    path('<int:pk>/', views.WishlistListView.as_view(), name='wishlist-detail'),





    # userfeedbacks
    path('', views.UserFeedbackListView.as_view(), name='userfeedback-list'),
    path('create/', views.UserFeedbackCreateView.as_view(), name='userfeedback-create'),
    path('update/<int:pk>/', views.UserFeedbackUpdateView.as_view(), name='userfeedback-update'),
    path('delete/<int:pk>/', views.UserFeedbackDeleteView.as_view(), name='userfeedback-delete'),
    path('<int:pk>/', views.UserFeedbackListView.as_view(), name='userfeedback-detail'),





    # errorlogs
    path('', views.ErrorLogListView.as_view(), name='errorlog-list'),
    path('create/', views.ErrorLogCreateView.as_view(), name='errorlog-create'),
    path('update/<int:pk>/', views.ErrorLogUpdateView.as_view(), name='errorlog-update'),
    path('delete/<int:pk>/', views.ErrorLogDeleteView.as_view(), name='errorlog-delete'),
    path('<int:pk>/', views.ErrorLogListView.as_view(), name='errorlog-detail'),


    path('api/1/', include(router.urls)),
    path('home/', views.home, name='home'),]
