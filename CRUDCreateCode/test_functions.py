import os
import pandas as pd
from config import *
import config


from utils.data_prep.find_model_names import get_file_names


def get_model_names(config):
    try:
        model_names = get_file_names(input_path=config.INPUT_PATH_MODELS)
        print(" --- Models:", model_names)
    except Exception as e:
        print(f"Error: {e}")
    return model_names

#model_names = get_model_names(config)
#print(model_names)


import os
import config
import pandas as pd
import os

def read_excel_sheets(file_path, sheet_names):
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    dataframes = {}
    for sheet_name in sheet_names:
        try:
            # Read each sheet into a separate DataFrame
            dataframes[sheet_name] = pd.read_excel(file_path, sheet_name=sheet_name)
        except Exception as e:
            raise Exception(f"An error occurred while reading the sheet '{sheet_name}': {e}")

    return dataframes

def read_model_settings(CURRENT_MODEL_NAME, config):
    file_path = config.INPUT_PATH_MODELS + CURRENT_MODEL_NAME + ".xlsx" # Replace with your file path
    try:
        df_model_setting = read_excel_sheets(file_path, config.sheet_names)
    except Exception as e:
        print(f"Error: {e}")
    return df_model_setting

# get the names of teh models to be run
def get_apps_names(config):
    try:
        model_names = get_file_names(input_path=config.INPUT_PATH_MODELS)
        print(" --- Models:", model_names)
    except Exception as e:
        print(f"Error: {e}")
    return model_names


apps_list = get_apps_names(config)
for i in apps_list:
    CURRENT_APP = i.split(".")[0]
    print("Current App: " + CURRENT_APP.split(".")[0])

    dfs = read_model_settings(CURRENT_APP, config)
    #print(dfs['model'].columns)
    print(dfs['model']['model_name'].unique())
    model_names = dfs['model']['model_name'].unique()
    for model_name in model_names:
        CURRENT_MODEL_NAME = model_name
        print(CURRENT_MODEL_NAME)