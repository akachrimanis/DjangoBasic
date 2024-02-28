

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

#from UserSession.models import UserSession  # Import your Customer model
# Define a function to generate fake UserSession data
def generate_fake_UserSessions(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user': fake.user(),
	'session_key': fake.session_key(),
	'start_time': fake.start_time(),
	'end_time': fake.end_time(),
	'ip_address': fake.address(),
         }
        data.append(record)
    return data
UserSession_data = generate_fake_UserSessions(num_records=config_fake_data.num_UserSession)

# Create a pandas DataFrame
df = pd.DataFrame(UserSession_data)

# Display the DataFrame
print(df)

#from Event.models import Event  # Import your Customer model
# Define a function to generate fake Event data
def generate_fake_Events(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user_session': fake.user_session(),
	'event_type': fake.event_type(),
	'timestamp': fake.timestamp(),
	'details': fake.details(),
         }
        data.append(record)
    return data
Event_data = generate_fake_Events(num_records=config_fake_data.num_Event)

# Create a pandas DataFrame
df = pd.DataFrame(Event_data)

# Display the DataFrame
print(df)

#from UserDevice.models import UserDevice  # Import your Customer model
# Define a function to generate fake UserDevice data
def generate_fake_UserDevices(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user_session': fake.user_session(),
	'device_details': fake.device_details(),
	'timestamp': fake.timestamp(),
         }
        data.append(record)
    return data
UserDevice_data = generate_fake_UserDevices(num_records=config_fake_data.num_UserDevice)

# Create a pandas DataFrame
df = pd.DataFrame(UserDevice_data)

# Display the DataFrame
print(df)

#from PageView.models import PageView  # Import your Customer model
# Define a function to generate fake PageView data
def generate_fake_PageViews(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user_session': fake.user_session(),
	'url': fake.url(),
	'timestamp': fake.timestamp(),
         }
        data.append(record)
    return data
PageView_data = generate_fake_PageViews(num_records=config_fake_data.num_PageView)

# Create a pandas DataFrame
df = pd.DataFrame(PageView_data)

# Display the DataFrame
print(df)

#from ClickEvent.models import ClickEvent  # Import your Customer model
# Define a function to generate fake ClickEvent data
def generate_fake_ClickEvents(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user_session': fake.user_session(),
	'element_id': fake.element_id(),
	'timestamp': fake.timestamp(),
         }
        data.append(record)
    return data
ClickEvent_data = generate_fake_ClickEvents(num_records=config_fake_data.num_ClickEvent)

# Create a pandas DataFrame
df = pd.DataFrame(ClickEvent_data)

# Display the DataFrame
print(df)

#from SearchQuery.models import SearchQuery  # Import your Customer model
# Define a function to generate fake SearchQuery data
def generate_fake_SearchQuerys(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user_session': fake.user_session(),
	'query': fake.query(),
	'timestamp': fake.timestamp(),
         }
        data.append(record)
    return data
SearchQuery_data = generate_fake_SearchQuerys(num_records=config_fake_data.num_SearchQuery)

# Create a pandas DataFrame
df = pd.DataFrame(SearchQuery_data)

# Display the DataFrame
print(df)

#from UserPreference.models import UserPreference  # Import your Customer model
# Define a function to generate fake UserPreference data
def generate_fake_UserPreferences(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user': fake.user(),
	'preferences': fake.preferences(),
         }
        data.append(record)
    return data
UserPreference_data = generate_fake_UserPreferences(num_records=config_fake_data.num_UserPreference)

# Create a pandas DataFrame
df = pd.DataFrame(UserPreference_data)

# Display the DataFrame
print(df)

#from CartActivity.models import CartActivity  # Import your Customer model
# Define a function to generate fake CartActivity data
def generate_fake_CartActivitys(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user_session': fake.user_session(),
	'activity_type': fake.activity_type(),
	'product': fake.product(),
	'quantity': fake.quantity(),
	'timestamp': fake.timestamp(),
         }
        data.append(record)
    return data
CartActivity_data = generate_fake_CartActivitys(num_records=config_fake_data.num_CartActivity)

# Create a pandas DataFrame
df = pd.DataFrame(CartActivity_data)

# Display the DataFrame
print(df)

#from Wishlist.models import Wishlist  # Import your Customer model
# Define a function to generate fake Wishlist data
def generate_fake_Wishlists(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user': fake.user(),
	'product': fake.product(),
	'added_on': fake.added_on(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
Wishlist_data = generate_fake_Wishlists(num_records=config_fake_data.num_Wishlist)

# Create a pandas DataFrame
df = pd.DataFrame(Wishlist_data)

# Display the DataFrame
print(df)

#from UserFeedback.models import UserFeedback  # Import your Customer model
# Define a function to generate fake UserFeedback data
def generate_fake_UserFeedbacks(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user_session': fake.user_session(),
	'feedback': fake.feedback(),
	'timestamp': fake.timestamp(),
         }
        data.append(record)
    return data
UserFeedback_data = generate_fake_UserFeedbacks(num_records=config_fake_data.num_UserFeedback)

# Create a pandas DataFrame
df = pd.DataFrame(UserFeedback_data)

# Display the DataFrame
print(df)

#from ErrorLog.models import ErrorLog  # Import your Customer model
# Define a function to generate fake ErrorLog data
def generate_fake_ErrorLogs(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user_session': fake.user_session(),
	'error_message': fake.error_message(),
	'timestamp': fake.timestamp(),
         }
        data.append(record)
    return data
ErrorLog_data = generate_fake_ErrorLogs(num_records=config_fake_data.num_ErrorLog)

# Create a pandas DataFrame
df = pd.DataFrame(ErrorLog_data)

# Display the DataFrame
print(df)

