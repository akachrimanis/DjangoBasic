import os
import config
import pandas as pd
import os

def read_excel_sheets(file_path, sheet_names):
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    dataframes = {}
    for sheet_name in sheet_names:
        try:
            # Read each sheet into a separate DataFrame
            dataframes[sheet_name] = pd.read_excel(file_path, sheet_name=sheet_name)
        except Exception as e:
            raise Exception(f"An error occurred while reading the sheet '{sheet_name}': {e}")

    return dataframes







# Create a list with the models to be read
# import pandas lib as pd
 
# read by default 1st sheet of an excel file
 
