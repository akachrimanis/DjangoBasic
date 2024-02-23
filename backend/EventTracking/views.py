from rest_framework import viewsets
from rest_framework import generics
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

def home(request):
    return render(request, "home.html",{})


from .models import UserSession, Event, UserDevice, PageView, ClickEvent, SearchQuery, UserPreference, CartActivity, Wishlist, UserFeedback, ErrorLog
from .forms import UserSessionForm, EventForm, UserDeviceForm, PageViewForm, ClickEventForm, SearchQueryForm, UserPreferenceForm, CartActivityForm, WishlistForm, UserFeedbackForm, ErrorLogForm
from .serializers import UserSessionSerializer, EventSerializer, UserDeviceSerializer, PageViewSerializer, ClickEventSerializer, SearchQuerySerializer, UserPreferenceSerializer, CartActivitySerializer, WishlistSerializer, UserFeedbackSerializer, ErrorLogSerializer

class UserSessionViewSet(viewsets.ModelViewSet):
    queryset = UserSession.objects.all()
    serializer_class = UserSessionSerializer
    
     # UserSession Views  
class UserSessionListView(ListView):
    model = UserSession
    template_name = 'usersession-list.html'
    context_object_name = 'usersessions'
    
class UserSessionDetailView(DetailView):
    model = UserSession
    template_name = 'usersession-details.html'
    context_object_name = 'usersessions'

class UserSessionCreateView(CreateView):
    model = UserSession
    form_class = UserSessionForm
    template_name = 'usersession-form.html'
    success_url = reverse_lazy('usersession-list')  # Redirect to the CRUD view after successful creation

class UserSessionUpdateView(UpdateView):
    model = UserSession
    form_class = UserSessionForm
    template_name = 'usersession-form.html'
    success_url = reverse_lazy('usersession-list')  # Redirect to the CRUD view after successful update

class UserSessionDeleteView(DeleteView):
    model = UserSession
    template_name = 'usersession-confirm-delete.html'
    success_url = reverse_lazy('usersession-list')  # Redirect to the CRUD view after successful deletion
   
    

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
     # Event Views  
class EventListView(ListView):
    model = Event
    template_name = 'event-list.html'
    context_object_name = 'events'
    
class EventDetailView(DetailView):
    model = Event
    template_name = 'event-details.html'
    context_object_name = 'events'

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event-form.html'
    success_url = reverse_lazy('event-list')  # Redirect to the CRUD view after successful creation

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'event-form.html'
    success_url = reverse_lazy('event-list')  # Redirect to the CRUD view after successful update

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'event-confirm-delete.html'
    success_url = reverse_lazy('event-list')  # Redirect to the CRUD view after successful deletion
   
    

class UserDeviceViewSet(viewsets.ModelViewSet):
    queryset = UserDevice.objects.all()
    serializer_class = UserDeviceSerializer
    
     # UserDevice Views  
class UserDeviceListView(ListView):
    model = UserDevice
    template_name = 'userdevice-list.html'
    context_object_name = 'userdevices'
    
class UserDeviceDetailView(DetailView):
    model = UserDevice
    template_name = 'userdevice-details.html'
    context_object_name = 'userdevices'

class UserDeviceCreateView(CreateView):
    model = UserDevice
    form_class = UserDeviceForm
    template_name = 'userdevice-form.html'
    success_url = reverse_lazy('userdevice-list')  # Redirect to the CRUD view after successful creation

class UserDeviceUpdateView(UpdateView):
    model = UserDevice
    form_class = UserDeviceForm
    template_name = 'userdevice-form.html'
    success_url = reverse_lazy('userdevice-list')  # Redirect to the CRUD view after successful update

class UserDeviceDeleteView(DeleteView):
    model = UserDevice
    template_name = 'userdevice-confirm-delete.html'
    success_url = reverse_lazy('userdevice-list')  # Redirect to the CRUD view after successful deletion
   
    

class PageViewViewSet(viewsets.ModelViewSet):
    queryset = PageView.objects.all()
    serializer_class = PageViewSerializer
    
     # PageView Views  
class PageViewListView(ListView):
    model = PageView
    template_name = 'pageview-list.html'
    context_object_name = 'pageviews'
    
class PageViewDetailView(DetailView):
    model = PageView
    template_name = 'pageview-details.html'
    context_object_name = 'pageviews'

class PageViewCreateView(CreateView):
    model = PageView
    form_class = PageViewForm
    template_name = 'pageview-form.html'
    success_url = reverse_lazy('pageview-list')  # Redirect to the CRUD view after successful creation

class PageViewUpdateView(UpdateView):
    model = PageView
    form_class = PageViewForm
    template_name = 'pageview-form.html'
    success_url = reverse_lazy('pageview-list')  # Redirect to the CRUD view after successful update

class PageViewDeleteView(DeleteView):
    model = PageView
    template_name = 'pageview-confirm-delete.html'
    success_url = reverse_lazy('pageview-list')  # Redirect to the CRUD view after successful deletion
   
    

class ClickEventViewSet(viewsets.ModelViewSet):
    queryset = ClickEvent.objects.all()
    serializer_class = ClickEventSerializer
    
     # ClickEvent Views  
class ClickEventListView(ListView):
    model = ClickEvent
    template_name = 'clickevent-list.html'
    context_object_name = 'clickevents'
    
class ClickEventDetailView(DetailView):
    model = ClickEvent
    template_name = 'clickevent-details.html'
    context_object_name = 'clickevents'

class ClickEventCreateView(CreateView):
    model = ClickEvent
    form_class = ClickEventForm
    template_name = 'clickevent-form.html'
    success_url = reverse_lazy('clickevent-list')  # Redirect to the CRUD view after successful creation

class ClickEventUpdateView(UpdateView):
    model = ClickEvent
    form_class = ClickEventForm
    template_name = 'clickevent-form.html'
    success_url = reverse_lazy('clickevent-list')  # Redirect to the CRUD view after successful update

class ClickEventDeleteView(DeleteView):
    model = ClickEvent
    template_name = 'clickevent-confirm-delete.html'
    success_url = reverse_lazy('clickevent-list')  # Redirect to the CRUD view after successful deletion
   
    

class SearchQueryViewSet(viewsets.ModelViewSet):
    queryset = SearchQuery.objects.all()
    serializer_class = SearchQuerySerializer
    
     # SearchQuery Views  
class SearchQueryListView(ListView):
    model = SearchQuery
    template_name = 'searchquery-list.html'
    context_object_name = 'searchquerys'
    
class SearchQueryDetailView(DetailView):
    model = SearchQuery
    template_name = 'searchquery-details.html'
    context_object_name = 'searchquerys'

class SearchQueryCreateView(CreateView):
    model = SearchQuery
    form_class = SearchQueryForm
    template_name = 'searchquery-form.html'
    success_url = reverse_lazy('searchquery-list')  # Redirect to the CRUD view after successful creation

class SearchQueryUpdateView(UpdateView):
    model = SearchQuery
    form_class = SearchQueryForm
    template_name = 'searchquery-form.html'
    success_url = reverse_lazy('searchquery-list')  # Redirect to the CRUD view after successful update

class SearchQueryDeleteView(DeleteView):
    model = SearchQuery
    template_name = 'searchquery-confirm-delete.html'
    success_url = reverse_lazy('searchquery-list')  # Redirect to the CRUD view after successful deletion
   
    

class UserPreferenceViewSet(viewsets.ModelViewSet):
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceSerializer
    
     # UserPreference Views  
class UserPreferenceListView(ListView):
    model = UserPreference
    template_name = 'userpreference-list.html'
    context_object_name = 'userpreferences'
    
class UserPreferenceDetailView(DetailView):
    model = UserPreference
    template_name = 'userpreference-details.html'
    context_object_name = 'userpreferences'

class UserPreferenceCreateView(CreateView):
    model = UserPreference
    form_class = UserPreferenceForm
    template_name = 'userpreference-form.html'
    success_url = reverse_lazy('userpreference-list')  # Redirect to the CRUD view after successful creation

class UserPreferenceUpdateView(UpdateView):
    model = UserPreference
    form_class = UserPreferenceForm
    template_name = 'userpreference-form.html'
    success_url = reverse_lazy('userpreference-list')  # Redirect to the CRUD view after successful update

class UserPreferenceDeleteView(DeleteView):
    model = UserPreference
    template_name = 'userpreference-confirm-delete.html'
    success_url = reverse_lazy('userpreference-list')  # Redirect to the CRUD view after successful deletion
   
    

class CartActivityViewSet(viewsets.ModelViewSet):
    queryset = CartActivity.objects.all()
    serializer_class = CartActivitySerializer
    
     # CartActivity Views  
class CartActivityListView(ListView):
    model = CartActivity
    template_name = 'cartactivity-list.html'
    context_object_name = 'cartactivitys'
    
class CartActivityDetailView(DetailView):
    model = CartActivity
    template_name = 'cartactivity-details.html'
    context_object_name = 'cartactivitys'

class CartActivityCreateView(CreateView):
    model = CartActivity
    form_class = CartActivityForm
    template_name = 'cartactivity-form.html'
    success_url = reverse_lazy('cartactivity-list')  # Redirect to the CRUD view after successful creation

class CartActivityUpdateView(UpdateView):
    model = CartActivity
    form_class = CartActivityForm
    template_name = 'cartactivity-form.html'
    success_url = reverse_lazy('cartactivity-list')  # Redirect to the CRUD view after successful update

class CartActivityDeleteView(DeleteView):
    model = CartActivity
    template_name = 'cartactivity-confirm-delete.html'
    success_url = reverse_lazy('cartactivity-list')  # Redirect to the CRUD view after successful deletion
   
    

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    
     # Wishlist Views  
class WishlistListView(ListView):
    model = Wishlist
    template_name = 'wishlist-list.html'
    context_object_name = 'wishlists'
    
class WishlistDetailView(DetailView):
    model = Wishlist
    template_name = 'wishlist-details.html'
    context_object_name = 'wishlists'

class WishlistCreateView(CreateView):
    model = Wishlist
    form_class = WishlistForm
    template_name = 'wishlist-form.html'
    success_url = reverse_lazy('wishlist-list')  # Redirect to the CRUD view after successful creation

class WishlistUpdateView(UpdateView):
    model = Wishlist
    form_class = WishlistForm
    template_name = 'wishlist-form.html'
    success_url = reverse_lazy('wishlist-list')  # Redirect to the CRUD view after successful update

class WishlistDeleteView(DeleteView):
    model = Wishlist
    template_name = 'wishlist-confirm-delete.html'
    success_url = reverse_lazy('wishlist-list')  # Redirect to the CRUD view after successful deletion
   
    

class UserFeedbackViewSet(viewsets.ModelViewSet):
    queryset = UserFeedback.objects.all()
    serializer_class = UserFeedbackSerializer
    
     # UserFeedback Views  
class UserFeedbackListView(ListView):
    model = UserFeedback
    template_name = 'userfeedback-list.html'
    context_object_name = 'userfeedbacks'
    
class UserFeedbackDetailView(DetailView):
    model = UserFeedback
    template_name = 'userfeedback-details.html'
    context_object_name = 'userfeedbacks'

class UserFeedbackCreateView(CreateView):
    model = UserFeedback
    form_class = UserFeedbackForm
    template_name = 'userfeedback-form.html'
    success_url = reverse_lazy('userfeedback-list')  # Redirect to the CRUD view after successful creation

class UserFeedbackUpdateView(UpdateView):
    model = UserFeedback
    form_class = UserFeedbackForm
    template_name = 'userfeedback-form.html'
    success_url = reverse_lazy('userfeedback-list')  # Redirect to the CRUD view after successful update

class UserFeedbackDeleteView(DeleteView):
    model = UserFeedback
    template_name = 'userfeedback-confirm-delete.html'
    success_url = reverse_lazy('userfeedback-list')  # Redirect to the CRUD view after successful deletion
   
    

class ErrorLogViewSet(viewsets.ModelViewSet):
    queryset = ErrorLog.objects.all()
    serializer_class = ErrorLogSerializer
    
     # ErrorLog Views  
class ErrorLogListView(ListView):
    model = ErrorLog
    template_name = 'errorlog-list.html'
    context_object_name = 'errorlogs'
    
class ErrorLogDetailView(DetailView):
    model = ErrorLog
    template_name = 'errorlog-details.html'
    context_object_name = 'errorlogs'

class ErrorLogCreateView(CreateView):
    model = ErrorLog
    form_class = ErrorLogForm
    template_name = 'errorlog-form.html'
    success_url = reverse_lazy('errorlog-list')  # Redirect to the CRUD view after successful creation

class ErrorLogUpdateView(UpdateView):
    model = ErrorLog
    form_class = ErrorLogForm
    template_name = 'errorlog-form.html'
    success_url = reverse_lazy('errorlog-list')  # Redirect to the CRUD view after successful update

class ErrorLogDeleteView(DeleteView):
    model = ErrorLog
    template_name = 'errorlog-confirm-delete.html'
    success_url = reverse_lazy('errorlog-list')  # Redirect to the CRUD view after successful deletion
   
    
