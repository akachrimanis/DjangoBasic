import os
import config
import pandas as pd
def create_admin(model_name, df):
    

# Register your models here.

    import_models = f"""from .models import Customer"""
    register_models = f"""admin.site.register({model_name})"""    
    return "from django.contrib import admin"


def save_file_py(my_string, output_path, model_name, file_name="admin.py"):
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

df = loaded_data["model"]

app_model_content = {}
for app_name in app_names:
    import_libs = f"""from django.contrib import admin\n"""
    import_models = "from .models import "
    admin_register = """admin.site.register("""
    register_models = ""
    model_names = df[df["app_name"]==app_name]["model_name"].unique().tolist()
    for model_name in model_names:
        register_models += f"""admin.site.register({model_name})\n"""    
        import_models += f"{model_name}, "

    content = import_libs + import_models[:-2] + "\n"  + register_models 
    save_file_py(content, config.BASIC_APP_PATH, app_name, file_name="admin.py") # ave teh app
    print(f"------{app_name}---------")
    print(content)
