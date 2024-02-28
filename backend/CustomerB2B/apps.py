
from django.apps import AppConfig


class CustomerB2BConfig(AppConfig):
    name = 'CustomerB2B'
    
    def ready(self):
        # Import signal handlers
        import CustomerB2B.signals

