def create_serializer(df, model_name):
    df = df.astype(str)


    # Starting script
    serializer_content = f"""\nfrom rest_framework import serializers\nfrom .models import {model_name}\n"""
    print(model_name)

    serializer_class = f"""\nclass {model_name}Serializer(serializers.ModelSerializer):\n
    class Meta:
        model = {model_name}
        fields = "__all__"
        
        """
        
    return serializer_content + serializer_class

import os
def save_serializers_py(my_string, output_path, model_name):
    file_name = "serializers.py"
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


import os
import config
import pandas as pd

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

model_names = find_model_names(loaded_data, column_name="model")
#print(find_app_names(loaded_data, column_name="model"))
app_names = find_app_names(loaded_data, column_name="model")


app_model_content = {}
for app_name in app_names:
    content = ""
    df = loaded_data['model'][loaded_data['model']["app_name"]==app_name]
    model_names = loaded_data['model'][loaded_data['model']["app_name"]==app_name]["model_name"].unique().tolist()
    print(model_names)
    for model_name in model_names:
        content += create_serializer(df, model_name)

    save_serializers_py(content, config.BASIC_APP_PATH, app_name)