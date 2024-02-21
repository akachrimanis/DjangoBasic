import shutil
import os
import shutil
import sys
from utils.dataIO.read_settings_xlsx import read_excel_to_dataframe

def replace_settings_file(current_folder, new_settings_folder):
    current_settings_path = os.path.join(current_folder, 'settings.py')
    new_settings_path = os.path.join(new_settings_folder, 'settings.py')
    
    try:
        # Copy settings.py to the new folder
        shutil.copy(new_settings_path, current_settings_path)
        print("Copy successful!")
    except FileNotFoundError:
        print("File not found. Please check the path provided.")
    except PermissionError:
        print("Permission denied. Make sure you have the necessary permissions.")


def add_installed_apps(df, model_name, config):
    import os

    # Define the path to your settings.py file
    settings_file_path = config.BASIC_APP_PATH+"settings.py"

    # List of apps you want to add
    apps_to_add = [{model_name}]

    # Read the contents of the settings.py file
    with open(settings_file_path, 'r') as f:
        lines = f.readlines()

    # Find the INSTALLED_APPS list and add the new apps to it
    for i, line in enumerate(lines):
        if line.strip().startswith('INSTALLED_APPS'):
            # Find the indentation level of INSTALLED_APPS
            indentation = line.index('INSTALLED_APPS')
            
            # Add the new apps with the appropriate indentation
            for app in apps_to_add:
                lines.insert(i + 1, ' ' * indentation + f"'{app}',\n")
            break

    # Write the modified contents back to the settings.py file
    with open(settings_file_path, 'w') as f:
        f.writelines(lines)

    print("Apps added to INSTALLED_APPS successfully.")


def add_installed_apps_on_txt(context, model_name, config):
    # Define the path to your settings.py file
    settings_file_path = config.BASIC_APP_PATH+"settings.py"

    # List of apps you want to add
    apps_to_add = [{model_name}]
    # Find the INSTALLED_APPS list and add the new apps to it
    for i, line in enumerate(context):
        if line.strip().startswith('INSTALLED_APPS'):
            # Find the indentation level of INSTALLED_APPS
            indentation = line.index('INSTALLED_APPS')
            
            # Add the new apps with the appropriate indentation
            for app in apps_to_add:
                context.insert(i + 1, ' ' * indentation + f"'{app}',\n")
                print({app})
            break

    return context



def create_settings(model_name, config):
    df = read_excel_to_dataframe(config.INPUT_PATH_SETTINGS, config.SETTINGS_FILENAME)
    #print(df)

    context = ""
    for i in df.index:
        if df.loc[i,'Variable'] == "libraries":
            context += f"""\n{df.loc[i,"settings_content"]}\n\n"""
        else:
            context += f"""\n{df.loc[i,"Variable"]} = {df.loc[i,"settings_content"]}"""

    context = add_installed_apps_on_txt(context, model_name, config)
    #print(context)

    apps_to_add = [model_name]
        # Find the INSTALLED_APPS list and add the new apps to it
    indentation = context.find("INSTALLED_APPS = [")
    # if line.strip().startswith('INSTALLED_APPS'):
            # Find the indentation level of INSTALLED_APPS
        # indentation = line.index('INSTALLED_APPS')
        
    for app in apps_to_add:
        output_line = context[:indentation+len("INSTALLED_APPS = [")] + f"""\n    {app},""" + context[indentation+len("INSTALLED_APPS = ["):]
    
    return output_line
