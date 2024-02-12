import shutil
import os
import shutil
import sys

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
