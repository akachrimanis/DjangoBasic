

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

#from CustomerB2C.models import CustomerB2C  # Import your Customer model
# Define a function to generate fake CustomerB2C data
def generate_fake_CustomerB2Cs(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'first_name' : fake.first_name(),
	'last_name' : fake.last_name(),
	'date_of_birth': fake.date_of_birth(),
	'email': fake.email(),
	'phone_number' : fake.phone_number(),
	'website' : fake.uri(),
	'address_line_1': fake.address(),
	'city': fake.city(),
	'state': fake.state(),
	'postal_code' : fake.zipcode(),
	'country': fake.country(),
	'notes' : fake.text(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
CustomerB2C_data = generate_fake_CustomerB2Cs(num_records=config_fake_data.num_CustomerB2C)

# Create a pandas DataFrame
df = pd.DataFrame(CustomerB2C_data)

# Display the DataFrame
print(df)

#from CustomerUserProfileB2C.models import CustomerUserProfileB2C  # Import your Customer model
# Define a function to generate fake CustomerUserProfileB2C data
def generate_fake_CustomerUserProfileB2Cs(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user_name' : fake.user_name(),
	'first_name' : fake.first_name(),
	'last_name' : fake.last_name(),
	'email': fake.email(),
	'phone_number' : fake.phone_number(),
	'last_login' : fake.date(),
         }
        data.append(record)
    return data
CustomerUserProfileB2C_data = generate_fake_CustomerUserProfileB2Cs(num_records=config_fake_data.num_CustomerUserProfileB2C)

# Create a pandas DataFrame
df = pd.DataFrame(CustomerUserProfileB2C_data)

# Display the DataFrame
print(df)

