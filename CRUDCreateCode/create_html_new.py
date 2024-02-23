import pandas as pd
import numpy as np

from config import *
import config

from utils.data_prep.create_html_basic import create_list_html,create_create_html, create_update_html, create_delete_html, create_detail_html, create_confirm_delete_html, create_form_html

from utils.dataIO.save_html_template import save_html_template




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


loaded_data = read_django_settings(file_name = config.INPUT_PATH_MODELS + "django-settings.pkl")
#print(loaded_data["model"])
def find_model_names(df, column_name="model"):
    return loaded_data[column_name]["model_name"].unique()
def find_app_names(df, column_name="model"):
    return loaded_data[column_name]["app_name"].unique()


    
#print(find_model_names(loaded_data, column_name="model"))
model_names = find_model_names(loaded_data, column_name="model")
#print(find_app_names(loaded_data, column_name="model"))
app_names = find_app_names(loaded_data, column_name="model")


app_model_content = {}
for app_name in app_names:
    df = loaded_data['model'][loaded_data['model']["app_name"]==app_name]
    
    # create html files
    model_names = loaded_data['model'][loaded_data['model']["app_name"]==app_name]["model_name"].unique().tolist()
    for CURRENT_MODEL_NAME in model_names:
        model_fields = df[df['model_name']==CURRENT_MODEL_NAME][df["filter_use"] == 1]["Variable"].tolist()

        list_html = create_list_html(df, CURRENT_MODEL_NAME)
        create_html = create_create_html(df, CURRENT_MODEL_NAME)
        update_html = create_update_html(df, CURRENT_MODEL_NAME)
        delete_html = create_delete_html(df, CURRENT_MODEL_NAME)
        detail_html = create_detail_html(df, CURRENT_MODEL_NAME, model_fields)
        confirm_delete = create_confirm_delete_html(df, CURRENT_MODEL_NAME)
        form_html = create_form_html(df, CURRENT_MODEL_NAME, model_fields)

        # save HTML files
        save_html_template(list_html, config.BASIC_APP_PATH, app_name, f"""{CURRENT_MODEL_NAME.lower()}-list.html""")
        save_html_template(create_html, config.BASIC_APP_PATH, app_name, f"{CURRENT_MODEL_NAME.lower()}-create.html")
        save_html_template(update_html, config.BASIC_APP_PATH, app_name, f"{CURRENT_MODEL_NAME.lower()}-update.html")
        save_html_template(delete_html, config.BASIC_APP_PATH, app_name, f"{CURRENT_MODEL_NAME.lower()}-delete.html")
        save_html_template(detail_html, config.BASIC_APP_PATH, app_name, f"{CURRENT_MODEL_NAME.lower()}-details.html")
        save_html_template(confirm_delete, config.BASIC_APP_PATH, app_name, f"{CURRENT_MODEL_NAME.lower()}-confirm-delete.html")
        save_html_template(form_html, config.BASIC_APP_PATH, app_name, f"{CURRENT_MODEL_NAME.lower()}-form.html")
