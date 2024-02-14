# myapp/management/commands/populate_data.py

import datetime
import random
from django.utils import timezone  # Import Django's timezone module
from django.core.management.base import BaseCommand
from Dashboardtestdata.models import Dashboardtestdata  # Replace 'myapp' with the name of your app


class Command(BaseCommand):
    help = 'Populates fake data for stock prices'

    def handle(self, *args, **kwargs):
        today = timezone.localdate()  # Use Django's timezone-aware version of today's date
        for i in range(12):
            # Calculate the month and year correctly
            month = today.month - i
            year = today.year
            if month <= 0:
                month += 12
                year -= 1
            month_start = timezone.datetime(year, month, 1).date()  # Make the datetime timezone-aware
            price = random.randint(1, 1000)  # Generate a random integer price between 1 and 1000
            Dashboardtestdata.objects.create(date=month_start, price=price)
        self.stdout.write(self.style.SUCCESS('Successfully populated fake data'))