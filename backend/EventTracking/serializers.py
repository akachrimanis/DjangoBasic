
from rest_framework import serializers
from .models import UserSession

class UserSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSession
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import UserDevice

class UserDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDevice
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import PageView

class PageViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = PageView
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import ClickEvent

class ClickEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClickEvent
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import SearchQuery

class SearchQuerySerializer(serializers.ModelSerializer):

    class Meta:
        model = SearchQuery
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import UserPreference

class UserPreferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPreference
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import CartActivity

class CartActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = CartActivity
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import Wishlist

class WishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wishlist
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import UserFeedback

class UserFeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFeedback
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import ErrorLog

class ErrorLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = ErrorLog
        fields = "__all__"
        
        
