import os
def save_model_py(my_string, output_path, model_name):
    file_name = "models.py"
    full_path = os.path.join(os.path.join(output_path,model_name), file_name)
    print(f"FILEPATH models.py: {full_path}")
# Writing the string to the file
    with open(full_path, 'a') as file:
        file.write(my_string + "\n")

    print(f"String has been saved to {full_path}")
