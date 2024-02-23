
import config
import  os
import pandas as pd

def read_django_settings(file_name = config.INPUT_PATH_MODELS + "django-settings.pkl"):
# Later, you can load the dictionary back from the pickle file
    loaded_data = pd.read_pickle(file_name)
    return loaded_data
            
def save_model_py(my_string, output_path, model_name):
    file_name = "models.py"
    full_path = os.path.join(os.path.join(output_path,model_name), file_name)
    print(f"FILEPATH models.py: {full_path}")
# Writing the string to the file
    with open(full_path, 'w') as file:
        file.write(my_string + "\n")

    print(f"String has been saved to {full_path}")


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


df = loaded_data["model"]
df_model_functions = loaded_data["model_functions"]
df_imports = loaded_data["imports"]

#df = df[df["filter_use"] == 1]
# Starting script
print(df_model_functions)
print(df_imports['functions'])
# create a list with all teh field types in the model variables

# create teh text for importing teh libraries of teh fieldtypes
fieldtypes_libraries = """from simple_history.models import HistoricalRecords\n"""
   
app_model_content = {}
app_models = {}

    #print(df_model_list)

for app_name in app_names:
    # import libraries
    
    model_imports = f"""from django.db import models\n"""
    model_imports += f"""{fieldtypes_libraries}\n"""
    model_definitions = ""
    
    df_model = df[df["app_name"]==app_name]
    model_names = df_model['model_name'].unique()
    df_model_functions = df_model_functions[df_model_functions["app_name"]==app_name]
    model_function_names = df_model_functions['model_name'].unique().tolist()
    df_imports = df_imports[df_imports["app_name"]==app_name]
    #imports_names = df_imports['functions'].unique()
    print(df_imports['functions'])
    imports_names=df_imports['functions'].unique()
    
    if imports_names.size > 0:
        for i in imports_names:
            model_imports += i + "\n"
            print("---------" + i)
    else:
        pass
            
    print(f"--------App: {app_name}")

    for model_name in model_names:
        model_content = f"""\n
class {model_name}(models.Model):\n"""
        model_variable_definition = ""
        for i in df_model[df_model["model_name"]==model_name].index:
            var_name = df_model[df_model["model_name"]==model_name].loc[i, "Variable"]
            args_name = df_model[df_model["model_name"]==model_name].loc[i, "Args"] 
            model_variable_definition += f"    {var_name} = {args_name} \n"
        model_definitions += model_content + model_variable_definition
        if model_name in model_function_names:
            for i in df_model_functions[df_model_functions["model_name"]==model_name].index:
                function_ = df_model_functions[df_model_functions["model_name"]==model_name].loc[i, "functions"]

                function_name = f"""\n{function_}\n""" 
                model_definitions += function_name

    #print(model_definitions)

    #print(model_imports + model_definitions)
    app_model_content[app_name] = model_imports + model_definitions

    save_model_py(app_model_content[app_name], config.BASIC_APP_PATH, app_name)

print(app_model_content["Organisation"])
