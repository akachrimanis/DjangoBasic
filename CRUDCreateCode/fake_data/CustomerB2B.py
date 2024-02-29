

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

#from CustomerB2B.models import CustomerB2B  # Import your Customer model
# Define a function to generate fake CustomerB2B data
def generate_fake_CustomerB2Bs(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'name': fake.name(),
	'email': fake.email(),
	'phone_number' : fake.phone_number(),
	'website' : fake.uri(),
	'address_line_1': fake.address(),
	'city': fake.city(),
	'state': fake.state(),
	'postal_code' : fake.zipcode(),
	'country': fake.country(),
	'contact_person': fake.contact_person(),
	'contact_email': fake.contact_email(),
	'contact_phone': fake.contact_phone(),
	'industry': fake.industry(),
	'company_size': fake.company_size(),
	'annual_revenue': fake.annual_revenue(),
	'tax_id': fake.tax_id(),
	'registration_number': fake.registration_number(),
	'payment_terms': fake.payment_terms(),
	'bank_name': fake.bank_name(),
	'bank_account_number': fake.bank_account_number(),
	'swift_code': fake.swift_code(),
	'company_group': fake.company_group(),
	'notes' : fake.text(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
CustomerB2B_data = generate_fake_CustomerB2Bs(num_records=config_fake_data.num_CustomerB2B)

# Create a pandas DataFrame
df = pd.DataFrame(CustomerB2B_data)

# Display the DataFrame
print(df)

#from CustomerB2BGoup.models import CustomerB2BGoup  # Import your Customer model
# Define a function to generate fake CustomerB2BGoup data
def generate_fake_CustomerB2BGoups(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'name': fake.name(),
	'email': fake.email(),
	'phone_number' : fake.phone_number(),
	'website' : fake.uri(),
	'address_line_1': fake.address(),
	'city': fake.city(),
	'state': fake.state(),
	'postal_code' : fake.zipcode(),
	'country': fake.country(),
	'industry': fake.industry(),
	'company_size': fake.company_size(),
	'annual_revenue': fake.annual_revenue(),
	'tax_id': fake.tax_id(),
	'registration_number': fake.registration_number(),
	'payment_terms': fake.payment_terms(),
	'bank_name': fake.bank_name(),
	'bank_account_number': fake.bank_account_number(),
	'swift_code': fake.swift_code(),
	'company_group': fake.company_group(),
	'notes' : fake.text(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
CustomerB2BGoup_data = generate_fake_CustomerB2BGoups(num_records=config_fake_data.num_CustomerB2BGoup)

# Create a pandas DataFrame
df = pd.DataFrame(CustomerB2BGoup_data)

# Display the DataFrame
print(df)

#from CustomerB2BAggregate_country.models import CustomerB2BAggregate_country  # Import your Customer model
# Define a function to generate fake CustomerB2BAggregate_country data
def generate_fake_CustomerB2BAggregate_countrys(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'country ': fake.country (),
	'total_customers ': fake.total_customers (),
	'total_annual_revenue ': fake.total_annual_revenue (),
	'total_industries ': fake.total_industries (),
	'total_company_size ': fake.total_company_size (),
         }
        data.append(record)
    return data
CustomerB2BAggregate_country_data = generate_fake_CustomerB2BAggregate_countrys(num_records=config_fake_data.num_CustomerB2BAggregate_country)

# Create a pandas DataFrame
df = pd.DataFrame(CustomerB2BAggregate_country_data)

# Display the DataFrame
print(df)

#from CustomerUserProfileB2B.models import CustomerUserProfileB2B  # Import your Customer model
# Define a function to generate fake CustomerUserProfileB2B data
def generate_fake_CustomerUserProfileB2Bs(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'company': fake.company(),
	'user_name' : fake.user_name(),
	'first_name' : fake.first_name(),
	'last_name' : fake.last_name(),
	'email': fake.email(),
	'phone_number' : fake.phone_number(),
	'description': fake.description(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
CustomerUserProfileB2B_data = generate_fake_CustomerUserProfileB2Bs(num_records=config_fake_data.num_CustomerUserProfileB2B)

# Create a pandas DataFrame
df = pd.DataFrame(CustomerUserProfileB2B_data)

# Display the DataFrame
print(df)

