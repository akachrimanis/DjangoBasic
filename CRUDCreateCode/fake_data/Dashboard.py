

import random
import sys
sys.path.append('/Users/tkax/dev/aimonetize/Backend/DjangoBasic/CRUDCreateCode')
import config
import config_fake_data

from faker import Faker
#from django.contrib.auth.models import User
from datetime import datetime
#import config
#import config_fake_data
import pandas as pd
fake = Faker()

# Generate a fake created_at timestamp within a specific range
def generate_fake_created_at(start_date, end_date):
    return fake.date_time_between(start_date=start_date, end_date=end_date)

# Example usage:
start_date = datetime(2020, 1, 1)  # Start date for the range
end_date = datetime.now()  # End date for the range (current date and time)
fake_created_at = generate_fake_created_at(start_date, end_date)

#from Dashboard.models import Dashboard  # Import your Customer model
# Define a function to generate fake Dashboard data
def generate_fake_Dashboards(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'date': fake.date(),
	'price': fake.price(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
Dashboard_data = generate_fake_Dashboards(num_records=config_fake_data.num_Dashboard)

# Create a pandas DataFrame
df = pd.DataFrame(Dashboard_data)

# Display the DataFrame
print(df)

