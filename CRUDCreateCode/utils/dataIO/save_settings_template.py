import os
def save_settings_py(my_string, output_path,):
    file_name = "settings.py"
    full_path = os.path.join(output_path, file_name)
    print(f"FILEPATH {file_name}: {full_path}")
# Writing the string to the file
    with open(full_path, 'w') as file:
        file.write(my_string + "\n")

    print(f"String has been saved to {full_path}")
