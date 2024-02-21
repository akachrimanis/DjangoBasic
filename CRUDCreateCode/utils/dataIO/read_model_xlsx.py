import os
import pandas as pd


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