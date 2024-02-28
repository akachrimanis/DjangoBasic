

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

#from Employee.models import Employee  # Import your Customer model
# Define a function to generate fake Employee data
def generate_fake_Employees(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'first_name': fake.first_name(),
	'last_name' : fake.last_name(),
	'age': fake.age(),
	'email': fake.email(),
	'phone_number' : fake.phone_number(),
	'address': fake.address(),
	'employer': fake.employer(),
	'manager': fake.manager(),
	'organization': fake.organization(),
         }
        data.append(record)
    return data
Employee_data = generate_fake_Employees(num_records=config_fake_data.num_Employee)

# Create a pandas DataFrame
df = pd.DataFrame(Employee_data)

# Display the DataFrame
print(df)

#from Individual.models import Individual  # Import your Customer model
# Define a function to generate fake Individual data
def generate_fake_Individuals(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user': fake.user(),
	'employee': fake.employee(),
         }
        data.append(record)
    return data
Individual_data = generate_fake_Individuals(num_records=config_fake_data.num_Individual)

# Create a pandas DataFrame
df = pd.DataFrame(Individual_data)

# Display the DataFrame
print(df)

#from Organization.models import Organization  # Import your Customer model
# Define a function to generate fake Organization data
def generate_fake_Organizations(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'name': fake.name(),
	'address': fake.address(),
         }
        data.append(record)
    return data
Organization_data = generate_fake_Organizations(num_records=config_fake_data.num_Organization)

# Create a pandas DataFrame
df = pd.DataFrame(Organization_data)

# Display the DataFrame
print(df)

#from Manager.models import Manager  # Import your Customer model
# Define a function to generate fake Manager data
def generate_fake_Managers(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'first_name': fake.first_name(),
	'last_name' : fake.last_name(),
	'age': fake.age(),
	'email': fake.email(),
	'phone_number' : fake.phone_number(),
	'address': fake.address(),
	'employer': fake.employer(),
	'organization': fake.organization(),
         }
        data.append(record)
    return data
Manager_data = generate_fake_Managers(num_records=config_fake_data.num_Manager)

# Create a pandas DataFrame
df = pd.DataFrame(Manager_data)

# Display the DataFrame
print(df)

#from Employer.models import Employer  # Import your Customer model
# Define a function to generate fake Employer data
def generate_fake_Employers(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'name': fake.name(),
	'email': fake.email(),
	'password': fake.password(),
	'company_name': fake.company_name(),
	'organization': fake.organization(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
Employer_data = generate_fake_Employers(num_records=config_fake_data.num_Employer)

# Create a pandas DataFrame
df = pd.DataFrame(Employer_data)

# Display the DataFrame
print(df)

