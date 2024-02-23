from django.contrib import admin
from .models import UserSession, Event, UserDevice, PageView, ClickEvent, SearchQuery, UserPreference, CartActivity, Wishlist, UserFeedback, ErrorLog
admin.site.register(UserSession)
admin.site.register(Event)
admin.site.register(UserDevice)
admin.site.register(PageView)
admin.site.register(ClickEvent)
admin.site.register(SearchQuery)
admin.site.register(UserPreference)
admin.site.register(CartActivity)
admin.site.register(Wishlist)
admin.site.register(UserFeedback)
admin.site.register(ErrorLog)

