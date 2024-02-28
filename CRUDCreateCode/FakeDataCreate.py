import os
import config
import pandas as pd
import pickle
import pandas as pd
import numpy as np
import config
from faker import Faker
from utils.data_prep.create_html_basic import create_list_html,create_create_html, create_update_html, create_delete_html, create_detail_html, create_confirm_delete_html, create_form_html
from datetime import datetime

from utils.dataIO.save_html_template import save_html_template
import config_fake_data
import config

class function_content:
    content = f"""\n
import random
import sys
sys.path.append('{config.BASIC_PATH}')
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
"""

    def content_end():
        content = f"""         }}
        data.append(record)
    return data"""
        return content
        
    def content_call_function(model_name):
        content = f"""
{model_name}_data = generate_fake_{model_name}s(num_records=config_fake_data.num_{model_name})

# Create a pandas DataFrame
df = pd.DataFrame({model_name}_data)

# Display the DataFrame
print(df)
"""
        return content
    def content_function(model_name):
        content = f"""
#from {model_name}.models import {model_name}  # Import your Customer model
# Define a function to generate fake {model_name} data
def generate_fake_{model_name}s(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {{
        # Generate fake data for specific fields
        """
        return content
      
def read_django_settings(file_name = config.INPUT_PATH_MODELS + "django-settings.pkl"):
# Later, you can load the dictionary back from the pickle file
    loaded_data = pd.read_pickle(file_name)
    return loaded_data
        
def create_file_if_not_exists(filename):
    try:
        with open(filename, 'x'):
            pass  # Do nothing if the file already exists
    except FileExistsError:
        print(f"File '{filename}' already exists")

import os

def save_fake_data_py(my_string, output_path, app_name):
    file_name = f"{app_name}.py"
    full_path = os.path.join(os.path.join(output_path,"fake_data"), file_name)
    print(f"FILEPATH {file_name}: {full_path}")
# Writing the string to the file
    try:
        with open(full_path, 'x'):
            pass  # Do nothing if the file already exists
    except FileNotFoundError:
        print(f"File '{full_path}' does not exist")
    except FileExistsError:
        print(f"File '{full_path}' already exists")
        
    with open(full_path, 'w') as file:
        file.write(my_string + "\n")

    print(f"String has been saved to {full_path}")
    
#print(loaded_data["model"])
def find_model_names(df, column_name="model"):
    return loaded_data[column_name]["model_name"].unique()
def find_app_names(df, column_name="model"):
    return loaded_data[column_name]["app_name"].unique()    

# Import data 
loaded_data = read_django_settings(file_name = config.INPUT_PATH_MODELS + "django-settings.pkl")



df = loaded_data['model'] # kep teh data in the xlsx sheet= model: where teh information of teh model are
model_names = loaded_data['model']["model_name"].unique().tolist() # create a list with all the models
app_names = loaded_data['model']["app_name"].unique().tolist()# create a list with all the apps 
variables_names = loaded_data['model']["Variable"].unique().tolist() # create a list with all the variables / fields
#print(len(variables_names))
#print(len(model_names))
#print(loaded_data['model']["Variable"].shape)

# make a selection of tables to start randomly.
df["faker_vars"] = df["Variable"].apply(lambda x: f"'{x}': fake.{x}()")
#print(df["faker_vars"].head())


list_skip_vars = ["history","department", "role", 'address_line_2'] # create list with teh variables to be excluded from fake data
model_dict = {} # empty dictionnairy for the models
app_dict ={} # empty dictionnairy for the apps
for app_name in app_names: # iterate on the apps
    print(f"---------{app_name} --------")
    df_app = df.loc[df['app_name'] == app_name] # select teh specific app in the loop
    model_names = df_app.loc[df['app_name']==app_name]["model_name"].unique().tolist() # # create a list with the models that belong in teh specific app in teh loop
    app_dict[app_name] = "" 

    for model_name in model_names:
        date_handler = 0
        content_faker = ""
        
        #print(f"---------{model_name} --------")
        df_model = df_app.loc[df['model_name'] == model_name]
        model_dict[model_name] = ""
        #print(df_model)
        for f in df_model.index:
            var_ = df_model.loc[f, "Variable"]
            if var_ in list_skip_vars:
                pass
            elif var_ in ["updated_at","created_at"]:
                if date_handler ==0:
                    content_faker += f"""\t'{var_}' : date_,\n"""  
                    date_handler +=1
                else:
                    content_faker += f"""\t'{var_}' : date_,\n"""    
                    date_handler +=1
            elif var_ == "website":
                content_faker += "\t'website' : fake.uri(),\n"
            elif var_ == "username":
                content_faker += "\t'user_name' : fake.user_name(),\n"
            elif var_ == "phone":
                content_faker += "\t'phone_number' : fake.phone_number(),\n"
            elif var_ == "firstname":
                content_faker += "\t'first_name' : fake.first_name(),\n"   
            elif var_ == "last_login":
                content_faker += "\t'last_login' : fake.date(),\n"
            elif var_ == "surname":
                content_faker += "\t'last_name' : fake.last_name(),\n"   
            elif var_ in ["notes", " description"]:
                content_faker += f"""\t'{var_}' : fake.text(),\n"""   
            elif "address" in var_:
                content_faker += f"""\t'{var_}': fake.address(),\n"""      
            elif "postal_code" == var_:
                content_faker += f"""\t'{var_}' : fake.zipcode(),\n"""  
            else:
                content_faker += "\t" + df_model.loc[f,"faker_vars"] + ",\n"
        #print(content_faker)
        #print(content_faker)
        model_dict[model_name] = function_content.content_function(model_name) + content_faker + function_content.content_end() + function_content.content_call_function(model_name)
        app_dict[app_name] += model_dict[model_name]
    app_dict[app_name] = function_content.content + app_dict[app_name]
    save_fake_data_py(app_dict[app_name], config_fake_data.BASIC_PATH, app_name)

    #print(app_dict[app_name])
    #print(f"{app_dict[app_name]}")

    

#content_dict[model_name] = content + content_faker + ")"
#print(content_dict)
# Call the function to generate fake customers

num_customers = 10  # Specify the number of fake customers to create
# CustomerB2C
# Create 100 Customers randomly based on the fields
# Define teh parameters for 
#- How ofthen they order
#- how much they spend
#- how often they visit teh website 

# Products
# Create 20 Products randomly based on the fields
# Create together teh poduct categories as part of teh products and then create the product category table

# Product Categories
# Derive

# Address


    
#print(model_dict["CustomerB2B"])

#print(df[["app_name","model_name","Variable", "faker_vars"]])
print(function_content.content)


#exec(app_dict["CustomerB2C"])