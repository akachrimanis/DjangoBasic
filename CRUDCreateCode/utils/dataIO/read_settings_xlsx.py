import os
import pandas as pd

def read_excel_to_dataframe(folder_path, file_name):
    # Construct the full file path
    file_path = os.path.join(folder_path, file_name)

    # Check if the folder exists
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")

    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    # Read the Excel file into a DataFrame
    try:
        dataframe = pd.read_excel(file_path)
        return dataframe
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {e}")
    
    
    return dataframe
