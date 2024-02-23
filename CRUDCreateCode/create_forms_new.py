import os
import config
import pandas as pd

def create_forms(df, model_name,app_name):
    df = df[df["filter_use"] == 1]

    form_fields = df[df['forms']==1][df["model_name"]==model_name]['Variable'].tolist()
    # print(form_fields)
    # Starting script
    forms_content = f"""
from .serializers import {model_name}Serializer
from .models import {model_name}\n


class {model_name}Form(forms.ModelForm):
    class Meta:
        model = {model_name}
        fields = {form_fields}
        # Add any other fields that you have in your Customer model\n
"""
    return forms_content


def save_file_py(my_string, output_path, model_name, file_name="forms.py"):
    full_path = os.path.join(os.path.join(output_path,model_name), file_name)
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




def read_django_settings(file_name = config.INPUT_PATH_MODELS + "django-settings.pkl"):
# Later, you can load the dictionary back from the pickle file
    loaded_data = pd.read_pickle(file_name)
    return loaded_data

def find_model_names(df, column_name="model"):
    return loaded_data[column_name]["model_name"].unique()
def find_app_names(df, column_name="model"):
    return loaded_data[column_name]["app_name"].unique()
#print(find_model_names(loaded_data, column_name="model"))


loaded_data = read_django_settings(file_name = config.INPUT_PATH_MODELS + "django-settings.pkl")

#print(find_app_names(loaded_data, column_name="model"))
app_names = find_app_names(loaded_data, column_name="model")


app_model_content = {}
for app_name in app_names:
    forms_content = f"""from django import forms"""
    df = loaded_data['model']
    model_names = df[df["app_name"]==app_name]["model_name"].unique().tolist()
    content_form = ""
    print(f"---------{app_name}-------------")
    print("----------------------")

    print(f"{model_names}")
    for model_name in model_names:
        content_form += create_forms(df, model_name,app_name)
    forms_content += content_form    
    save_file_py(forms_content, config.BASIC_APP_PATH, app_name, file_name="forms.py")
    
    #app_model_content[forms_content]