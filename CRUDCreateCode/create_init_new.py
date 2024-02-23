import os
import config
import pandas as pd
def save_file_py(my_string, output_path, app_name, file_name="__init__.py.py"):
    full_path = os.path.join(os.path.join(output_path,app_name), file_name)
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


for app_name in app_names:
    content = f"""default_app_config = '{app_name}.apps.{app_name}Config'"""

    save_file_py(content, config.BASIC_APP_PATH, app_name, file_name="__init__.py")