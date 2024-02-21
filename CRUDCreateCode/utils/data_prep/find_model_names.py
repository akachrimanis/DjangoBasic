import os
import pathlib

def get_file_names(input_path):
    # Check if the given path is actually a directory
    if not os.path.isdir(input_path):
        raise ValueError(f"The path {input_path} is not a directory.")
    illegalchar = ['/' ,':' ,'*', '?', '"', '<', '>', '|', '.', '~']

    file_names = []
    # os.listdir returns a list containing the names of the entries in the directory given by path
    for entry in os.listdir(input_path):
        # Join the path and entry to get full path
        # print(entry)
        if "$" not in entry and "~" not in entry:
            full_path = os.path.join(input_path, entry)
        # Check if it's a file and not a directory
        if os.path.isfile(full_path):
            if entry[0] not in illegalchar:
                file_names.append(entry)

    return file_names

