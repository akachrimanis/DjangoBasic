import os
def save_html_template(my_string, output_path, model_name, file_name):
    # checking if the directory demo_folder  
    # exist or not. 
    model_template_dir = os.path.exists(os.path.join(output_path,"templates/" + model_name))
    print(model_template_dir)

    if not os.path.exists(model_template_dir):  
    # if the demo_folder directory is not present  
    # then create it. 
        os.makedirs(os.path.join(output_path,"templates/" + model_name))  
        print(" Folder was created!!!")
    try:
        os.makedirs(os.path.join(output_path,"templates/" + model_name))
    except FileExistsError:
    # directory already exists
        pass     
    full_path = os.path.join(output_path,"templates/" + model_name + "/" +  file_name)
    print(f"FILEPATH html.py: {full_path}")
# Writing the string to the file
    with open(full_path, 'w') as file:
        file.write(my_string + "\n")

    print(f"String has been saved to {full_path}")
