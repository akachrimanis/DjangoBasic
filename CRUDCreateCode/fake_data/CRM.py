

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

#from InteractionType.models import InteractionType  # Import your Customer model
# Define a function to generate fake InteractionType data
def generate_fake_InteractionTypes(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'name': fake.name(),
         }
        data.append(record)
    return data
InteractionType_data = generate_fake_InteractionTypes(num_records=config_fake_data.num_InteractionType)

# Create a pandas DataFrame
df = pd.DataFrame(InteractionType_data)

# Display the DataFrame
print(df)

#from Interaction.models import Interaction  # Import your Customer model
# Define a function to generate fake Interaction data
def generate_fake_Interactions(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user': fake.user(),
	'date': fake.date(),
	'interaction_type': fake.interaction_type(),
	'notes' : fake.text(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
Interaction_data = generate_fake_Interactions(num_records=config_fake_data.num_Interaction)

# Create a pandas DataFrame
df = pd.DataFrame(Interaction_data)

# Display the DataFrame
print(df)

#from InteractionDetails.models import InteractionDetails  # Import your Customer model
# Define a function to generate fake InteractionDetails data
def generate_fake_InteractionDetailss(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'interaction': fake.interaction(),
	'details': fake.details(),
	'handled_by': fake.handled_by(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
InteractionDetails_data = generate_fake_InteractionDetailss(num_records=config_fake_data.num_InteractionDetails)

# Create a pandas DataFrame
df = pd.DataFrame(InteractionDetails_data)

# Display the DataFrame
print(df)

#from TaskType.models import TaskType  # Import your Customer model
# Define a function to generate fake TaskType data
def generate_fake_TaskTypes(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'name': fake.name(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
TaskType_data = generate_fake_TaskTypes(num_records=config_fake_data.num_TaskType)

# Create a pandas DataFrame
df = pd.DataFrame(TaskType_data)

# Display the DataFrame
print(df)

#from Task.models import Task  # Import your Customer model
# Define a function to generate fake Task data
def generate_fake_Tasks(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'customer': fake.customer(),
	'task_type': fake.task_type(),
	'due_date': fake.due_date(),
	'description': fake.description(),
	'assigned_to': fake.assigned_to(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
Task_data = generate_fake_Tasks(num_records=config_fake_data.num_Task)

# Create a pandas DataFrame
df = pd.DataFrame(Task_data)

# Display the DataFrame
print(df)

