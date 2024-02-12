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


def main():
    
   # Create the folder structure
    create_main_folders(config)
    print("Template folder path:" + template_mystaticfiles_PATH)
    print("Source folder css:" + config.SOURCE_FOLDER_CSS)
    print("Destinations folder css:" + config.DESTINATION_FOLDER_CSS)
    copy_file_to_destination(config.SOURCE_FOLDER_CSS,config.DESTINATION_FOLDER_CSS)
    
    # get the names of teh models to be run
    try:
        model_names = get_file_names(input_path=INPUT_PATH_MODELS)
        print(" --- Models:", model_names[0])
    except Exception as e:
        print(f"Error: {e}")

    # Read the setting.xlsx
    try:
        df_settings = read_excel_to_dataframe(INPUT_PATH_SETTINGS, SETTINGS_FILENAME)
        print("SETTINGS loaded successfully.")
        #print(df_settings.head())  # Display the first few rows of the DataFrame
    except Exception as e:
        print(f"Error: {e}")

    print("Source settings.py: " + SOURCE_FOLDER_SETTINGS)
    print("Destination settings.py: " + BACKEND_MAINAPP_PATH)

    # replace settings file
    replace_settings_file(config.BACKEND_MAINAPP_PATH,config.SOURCE_FOLDER_SETTINGS)
        
    # Read the setting for the model creation from the file model.xlsx
    # Example usage
    CURRENT_MODEL_NAME = model_names[0].split(".")[0]
    print("Current model created: " + CURRENT_MODEL_NAME)
    file_path = INPUT_PATH_MODELS + CURRENT_MODEL_NAME + ".xlsx" # Replace with your file path
    sheet_names = ['model','model_functions', 'serializers', 'views', 'html', 'forms', "urls"]

    try:
        df_model_setting = read_excel_sheets(file_path, sheet_names)
        print("\nThe sheets of model settings are:")
        for name, df in df_model_setting.items():
            print(f"Data from sheet '{name}':")
            #print(df.head())  # Display the first few rows of each DataFrame
    except Exception as e:
        print(f"Error: {e}")
        
    # Create the text for the models.py file 
    # Create the model parameters and definitions
    model_definitions = create_model(df_model_setting['model'], model_name=CURRENT_MODEL_NAME)
    print("\n The model's variables are:")
    print(df_model_setting['model'][df_model_setting['model']["filter_use"] == "True"]["Variable"].tolist())
    
    model_fields = df_model_setting['model'][df_model_setting['model']["filter_use"] == "True"]["Variable"].tolist()
    #df_model_setting['model'] = df_model_setting['model'][df["filter_use"] == "True"]
    # create the functionality
    model_functionality = create_functionality(df_model_setting['model_functions'])
    models_py_str = model_definitions + "\n" + model_functionality

    # Save the models.py file accordingly
    print(models_py_str)
    save_model_py(models_py_str, BASIC_APP_PATH, CURRENT_MODEL_NAME)  
    
    ## serializers.py
    # Create serializers.py
    serializers_py_str = create_serializer(df_model_setting['serializers'], CURRENT_MODEL_NAME)

    # Save serializer.py
    save_serializers_py(serializers_py_str, BASIC_APP_PATH, CURRENT_MODEL_NAME)

    ## views.py

    # Create views.py
    views_py_str = create_views(df_model_setting['views'], CURRENT_MODEL_NAME)

    # Save views.py
    save_views_py(views_py_str, BASIC_APP_PATH, CURRENT_MODEL_NAME)

    ## urls.py
    # Create urls.py
    urls_py_str = create_urls(df_model_setting['urls'], CURRENT_MODEL_NAME)

    # Save urls.py
    save_urls_py(urls_py_str, BASIC_APP_PATH, CURRENT_MODEL_NAME)

    ## forms.py
    # Create forms.py
    forms_py_str = create_forms(df_model_setting['model'], CURRENT_MODEL_NAME)

    # Save forms.py 
    save_forms_py(forms_py_str, BASIC_APP_PATH, CURRENT_MODEL_NAME)

    # create html files
    list_html = create_list_html(df_model_setting['model'], CURRENT_MODEL_NAME)
    create_html = create_create_html(df_model_setting['model'], CURRENT_MODEL_NAME)
    update_html = create_update_html(df_model_setting['model'], CURRENT_MODEL_NAME)
    delete_html = create_delete_html(df_model_setting['model'], CURRENT_MODEL_NAME)
    detail_html = create_detail_html(df_model_setting['model'], CURRENT_MODEL_NAME, model_fields)
    confirm_delete = create_confirm_delete_html(df_model_setting['model'], CURRENT_MODEL_NAME)
    form_html = create_form_html(df_model_setting['model'], CURRENT_MODEL_NAME, model_fields)
    
    # save HTML files
    save_html_template(list_html, BASIC_APP_PATH, CURRENT_MODEL_NAME, f"""{CURRENT_MODEL_NAME.lower()}-list.html""")
    save_html_template(create_html, BASIC_APP_PATH, CURRENT_MODEL_NAME, f"{CURRENT_MODEL_NAME.lower()}-create.html")
    save_html_template(update_html, BASIC_APP_PATH, CURRENT_MODEL_NAME, f"{CURRENT_MODEL_NAME.lower()}-update.html")
    save_html_template(delete_html, BASIC_APP_PATH, CURRENT_MODEL_NAME, f"{CURRENT_MODEL_NAME.lower()}-delete.html")
    save_html_template(detail_html, BASIC_APP_PATH, CURRENT_MODEL_NAME, f"{CURRENT_MODEL_NAME.lower()}-details.html")
    save_html_template(confirm_delete, BASIC_APP_PATH, CURRENT_MODEL_NAME, f"{CURRENT_MODEL_NAME.lower()}-confirm-delete.html")
    save_html_template(form_html, BASIC_APP_PATH, CURRENT_MODEL_NAME, f"{CURRENT_MODEL_NAME.lower()}-form.html")

    
    # Create the admin.py
    admin_py_str = create_admin(df_model_setting['model'], CURRENT_MODEL_NAME)
    save_admin_py(admin_py_str, BASIC_APP_PATH, CURRENT_MODEL_NAME)
    # create the settings
    # installed_apps
    # template_dirs
if __name__ == "__main__":
    main()