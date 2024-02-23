from django import forms
from .serializers import UserSessionSerializer
from .models import UserSession



class UserSessionForm(forms.ModelForm):
    class Meta:
        model = UserSession
        fields = ['user', 'session_key', 'start_time', 'end_time', 'ip_address']
        # Add any other fields that you have in your Customer model


from .serializers import EventSerializer
from .models import Event



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['user_session', 'event_type', 'timestamp', 'details']
        # Add any other fields that you have in your Customer model


from .serializers import UserDeviceSerializer
from .models import UserDevice



class UserDeviceForm(forms.ModelForm):
    class Meta:
        model = UserDevice
        fields = ['user_session', 'device_details', 'timestamp']
        # Add any other fields that you have in your Customer model


from .serializers import PageViewSerializer
from .models import PageView



class PageViewForm(forms.ModelForm):
    class Meta:
        model = PageView
        fields = ['user_session', 'url', 'timestamp']
        # Add any other fields that you have in your Customer model


from .serializers import ClickEventSerializer
from .models import ClickEvent



class ClickEventForm(forms.ModelForm):
    class Meta:
        model = ClickEvent
        fields = ['user_session', 'element_id', 'timestamp']
        # Add any other fields that you have in your Customer model


from .serializers import SearchQuerySerializer
from .models import SearchQuery



class SearchQueryForm(forms.ModelForm):
    class Meta:
        model = SearchQuery
        fields = ['user_session', 'query', 'timestamp']
        # Add any other fields that you have in your Customer model


from .serializers import UserPreferenceSerializer
from .models import UserPreference



class UserPreferenceForm(forms.ModelForm):
    class Meta:
        model = UserPreference
        fields = ['user', 'preferences']
        # Add any other fields that you have in your Customer model


from .serializers import CartActivitySerializer
from .models import CartActivity



class CartActivityForm(forms.ModelForm):
    class Meta:
        model = CartActivity
        fields = ['user_session', 'activity_type', 'product', 'quantity', 'timestamp']
        # Add any other fields that you have in your Customer model


from .serializers import WishlistSerializer
from .models import Wishlist



class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['user', 'product', 'added_on']
        # Add any other fields that you have in your Customer model


from .serializers import UserFeedbackSerializer
from .models import UserFeedback



class UserFeedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = ['user_session', 'feedback', 'timestamp']
        # Add any other fields that you have in your Customer model


from .serializers import ErrorLogSerializer
from .models import ErrorLog



class ErrorLogForm(forms.ModelForm):
    class Meta:
        model = ErrorLog
        fields = ['user_session', 'error_message', 'timestamp']
        # Add any other fields that you have in your Customer model


