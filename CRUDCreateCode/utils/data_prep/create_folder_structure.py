


import os
import shutil



def create_folder_if_not_exists(folder_path):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")

def create_main_folders(config):
    # mystaticfiles: Create if does not exist
    create_folder_if_not_exists(config.MAIN_APP_mystaticfiles_PATH)
    # media
    create_folder_if_not_exists(config.MAIN_APP_media_PATH)
    # templates
    create_folder_if_not_exists(config.MAIN_APP_templates_PATH)



def copy_file_to_destination(source_path, destination_path):
    # Make sure the destination directory exists; create it if it doesn't
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    # Copy the file
    shutil.copy(source_path, destination_path)

    print(f"File copied from {source_path} to {destination_path}")

