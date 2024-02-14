import pathlib
import os
import math 
import pandas as pd
import numpy as np

from config import *
import config

from utils.data_prep.create_folder_structure import create_main_folders, copy_file_to_destination
from utils.data_prep.create_model import create_model, create_functionality
from utils.data_prep.create_serializer import create_serializer
from utils.data_prep.create_urls import create_urls
from utils.data_prep.create_views import create_views
from utils.data_prep.create_forms import create_forms
from utils.data_prep.create_html_basic import create_list_html,create_create_html, create_update_html, create_delete_html, create_detail_html, create_confirm_delete_html, create_form_html
from utils.data_prep.find_model_names import get_file_names
from utils.data_prep.create_settings import replace_settings_file
from utils.data_prep.create_admin import create_admin
from utils.data_prep.create_charts import *
from utils.dataIO.read_settings_xlsx import read_excel_to_dataframe
from utils.dataIO.read_model_xlsx import read_excel_sheets 
from utils.dataIO.save_serializer_template import save_serializers_py
from utils.dataIO.save_model_template import save_model_py
from utils.dataIO.save_views_template import save_views_py
from utils.dataIO.save_urls_template import save_urls_py
from utils.dataIO.save_forms_template import save_forms_py
from utils.dataIO.save_html_template import save_html_template
from utils.dataIO.save_admin import save_admin_py

print("INPUT_PATH_MODELS" + BASIC_PATH, "\nINPUT_PATH_SETTINGS" + INPUT_PATH_SETTINGS, "\nINPUT_PATH_MODELS" + INPUT_PATH_MODELS)
    
# Create the folder structure
def main_create_folders(config):
    try:
        create_main_folders(config)
        print("Template folder path:" + config.template_mystaticfiles_PATH)
        print("Source folder css:" + config.SOURCE_FOLDER_CSS)
        print("Destinations folder css:" + config.DESTINATION_FOLDER_CSS)
    except Exception as e:
        print(f"Error: {e}")    
    try:
        copy_file_to_destination(config.SOURCE_FOLDER_CSS,config.DESTINATION_FOLDER_CSS)
    except Exception as e:
        print(f"Error: {e}")          

# get the names of teh models to be run
def get_model_names(config):
    try:
        model_names = get_file_names(input_path=config.INPUT_PATH_MODELS)
        print(" --- Models:", model_names)
    except Exception as e:
        print(f"Error: {e}")
    return model_names

def read_settings(config):
# Read the setting.xlsx
    try:
        df_settings = read_excel_to_dataframe(config.INPUT_PATH_SETTINGS, config.SETTINGS_FILENAME)
        print("SETTINGS loaded successfully.")
        #print(df_settings.head())  # Display the first few rows of the DataFrame
    except Exception as e:
        print(f"Error: {e}")
        
    # replace settings file
    print("Source settings.py: " + config.SOURCE_FOLDER_SETTINGS)
    print("Destination settings.py: " + config.BACKEND_MAINAPP_PATH)
    replace_settings_file(config.BACKEND_MAINAPP_PATH, config.SOURCE_FOLDER_SETTINGS)
    
    return df_settings
# Read the setting for the model creation from the file model.xlsx
# Example usage
def read_model_settings(CURRENT_MODEL_NAME, config):
    file_path = config.INPUT_PATH_MODELS + CURRENT_MODEL_NAME + ".xlsx" # Replace with your file path
    try:
        df_model_setting = read_excel_sheets(file_path, config.sheet_names)
    except Exception as e:
        print(f"Error: {e}")
    return df_model_setting


def create_one_model(CURRENT_MODEL_NAME, df_model_setting, config):
    print(f"------------------------------------")
    print(f"-------{CURRENT_MODEL_NAME}-----------")
    print(f"-------      Models     -----------")
        
    # Create the text for the models.py file 
    # Create the model parameters and definitions
    model_definitions = create_model(df_model_setting['model'], model_name=CURRENT_MODEL_NAME)
    print(f"\n - The {CURRENT_MODEL_NAME} model's variables are:")
    print(df_model_setting['model'][df_model_setting['model']["filter_use"] == "True"]["Variable"].tolist())
    
    #model_fields = df_model_setting['model'][df_model_setting['model']["filter_use"] == "True"]["Variable"].tolist()
    #df_model_setting['model'] = df_model_setting['model'][df["filter_use"] == "True"]
    # create the functionality
    model_functionality = create_functionality(df_model_setting['model_functions'])
    models_py_str = model_definitions + "\n" + model_functionality

    # Save the models.py file accordingly
    print(f"The {CURRENT_MODEL_NAME} model: ")
    print(models_py_str)
    save_model_py(models_py_str, config.BASIC_APP_PATH, CURRENT_MODEL_NAME)  
    
def create_one_serializer(CURRENT_MODEL_NAME, df_model_setting, config):
    ## serializers.py
    # Create serializers.py
    print(f"-------  Serializers  -----------")

    serializers_py_str = create_serializer(df_model_setting['serializers'], CURRENT_MODEL_NAME)

    # Save serializer.py
    save_serializers_py(serializers_py_str, config.BASIC_APP_PATH, CURRENT_MODEL_NAME)

def create_one_views(CURRENT_MODEL_NAME, df_model_setting, config):
    ## views.py
    # Create views.py
    views_py_str = create_views(df_model_setting['views'], CURRENT_MODEL_NAME)

    # Save views.py
    save_views_py(views_py_str, config.BASIC_APP_PATH, CURRENT_MODEL_NAME)

def create_one_urls(CURRENT_MODEL_NAME, df_model_setting, config):
    ## urls.py
    # Create urls.py
    urls_py_str = create_urls(df_model_setting['urls'], CURRENT_MODEL_NAME)

    # Save urls.py
    save_urls_py(urls_py_str, config.BASIC_APP_PATH, CURRENT_MODEL_NAME)
    
def create_one_admin(CURRENT_MODEL_NAME, df_model_setting, config):
    # Create the admin.py
    admin_py_str = create_admin(df_model_setting['model'], CURRENT_MODEL_NAME)
    
    # Save admin.py 
    save_admin_py(admin_py_str, config.BASIC_APP_PATH, CURRENT_MODEL_NAME)

def create_one_forms(CURRENT_MODEL_NAME, df_model_setting, config):
    ## forms.py
    # Create forms.py
    forms_py_str = create_forms(df_model_setting['model'], CURRENT_MODEL_NAME)

    # Save forms.py 
    save_forms_py(forms_py_str, config.BASIC_APP_PATH, CURRENT_MODEL_NAME)

def create_one_html(CURRENT_MODEL_NAME, df_model_setting, config):
    model_fields = df_model_setting['model'][df_model_setting['model']["filter_use"] == "True"]["Variable"].tolist()

    # create html files
    list_html = create_list_html(df_model_setting['model'], CURRENT_MODEL_NAME)
    create_html = create_create_html(df_model_setting['model'], CURRENT_MODEL_NAME)
    update_html = create_update_html(df_model_setting['model'], CURRENT_MODEL_NAME)
    delete_html = create_delete_html(df_model_setting['model'], CURRENT_MODEL_NAME)
    detail_html = create_detail_html(df_model_setting['model'], CURRENT_MODEL_NAME, model_fields)
    confirm_delete = create_confirm_delete_html(df_model_setting['model'], CURRENT_MODEL_NAME)
    form_html = create_form_html(df_model_setting['model'], CURRENT_MODEL_NAME, model_fields)
    
    # save HTML files
    save_html_template(list_html, config.BASIC_APP_PATH, CURRENT_MODEL_NAME, f"""{CURRENT_MODEL_NAME.lower()}-list.html""")
    save_html_template(create_html, config.BASIC_APP_PATH, CURRENT_MODEL_NAME, f"{CURRENT_MODEL_NAME.lower()}-create.html")
    save_html_template(update_html, config.BASIC_APP_PATH, CURRENT_MODEL_NAME, f"{CURRENT_MODEL_NAME.lower()}-update.html")
    save_html_template(delete_html, config.BASIC_APP_PATH, CURRENT_MODEL_NAME, f"{CURRENT_MODEL_NAME.lower()}-delete.html")
    save_html_template(detail_html, config.BASIC_APP_PATH, CURRENT_MODEL_NAME, f"{CURRENT_MODEL_NAME.lower()}-details.html")
    save_html_template(confirm_delete, config.BASIC_APP_PATH, CURRENT_MODEL_NAME, f"{CURRENT_MODEL_NAME.lower()}-confirm-delete.html")
    save_html_template(form_html, config.BASIC_APP_PATH, CURRENT_MODEL_NAME, f"{CURRENT_MODEL_NAME.lower()}-form.html")
    
# create charts
def create_one_chart(df, model_name):
    CURRENT_MODEL_NAME = model_name.split(".")[0] # CURRENT_MODEL_NAME

    chart = create_chart(df, CURRENT_MODEL_NAME, 'line')
    save_html_template(chart, config.BASIC_APP_PATH, CURRENT_MODEL_NAME, f"""{CURRENT_MODEL_NAME.lower()}-line.html""")
    chart = create_chart(df, CURRENT_MODEL_NAME, 'bubble')
    save_html_template(chart, config.BASIC_APP_PATH, CURRENT_MODEL_NAME, f"""{CURRENT_MODEL_NAME.lower()}-bubble.html""")
    chart = create_chart(df, CURRENT_MODEL_NAME, 'bar')
    save_html_template(chart, config.BASIC_APP_PATH, CURRENT_MODEL_NAME, f"""{CURRENT_MODEL_NAME.lower()}-bar.html""")    
    chart = create_chart(df, CURRENT_MODEL_NAME, 'bubble')
    save_html_template(chart, config.BASIC_APP_PATH, CURRENT_MODEL_NAME, f"""{CURRENT_MODEL_NAME.lower()}-bubble.html""")    
    chart = create_chart(df, CURRENT_MODEL_NAME, 'scatter')
    save_html_template(chart, config.BASIC_APP_PATH, CURRENT_MODEL_NAME, f"""{CURRENT_MODEL_NAME.lower()}-scatter.html""")    
    chart = create_chart(df, CURRENT_MODEL_NAME, 'radar')
    save_html_template(chart, config.BASIC_APP_PATH, CURRENT_MODEL_NAME, f"""{CURRENT_MODEL_NAME.lower()}-radar.html""")
def create_django_functions(model_name, config, models=1, serializers=1, urls=1, views=1, admin=1, forms=1, html=1):
        """Create all teh files and functions for one model"""
        
        CURRENT_MODEL_NAME = model_name.split(".")[0] # CURRENT_MODEL_NAME
        df_model_setting = read_model_settings(CURRENT_MODEL_NAME, config) # Model configuration
        create_one_model(CURRENT_MODEL_NAME, df_model_setting, config) # models.py
        create_one_serializer(CURRENT_MODEL_NAME, df_model_setting, config) # serializers
        create_one_urls(CURRENT_MODEL_NAME, df_model_setting, config) # urls
        create_one_views(CURRENT_MODEL_NAME, df_model_setting, config) # views
        create_one_admin(CURRENT_MODEL_NAME, df_model_setting, config) #admin
        create_one_forms(CURRENT_MODEL_NAME, df_model_setting, config) # forms
        create_one_html(CURRENT_MODEL_NAME, df_model_setting, config) # html


# create the settings
# installed_apps
# template_dirs
def main():
    # main_create_folders(config)
    model_names = get_model_names(config)
    for model_name in model_names:
        create_django_functions(model_name, config, models=1, serializers=1, urls=0, views=0, admin=0, forms=0, html=0)

if __name__ == "__main__":
    main()
