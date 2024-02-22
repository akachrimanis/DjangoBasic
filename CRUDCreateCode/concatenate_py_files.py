import config
from utils.dataIO.read_model_xlsx import *

def concatenate_py_files(config):
    MODELS_LIST = []
    dataframes_py = {}
    df_py_list = {}
    
    for app_ in config.APP_NAMES:
        dataframes_py[app_] = {}
        for py in config.sheet_names: # Create a disctionnairy of dataframes for each .py file of teh django app
            if 'help' not in py:
                dataframes_py[app_][py]=[]
            #print("App:" + app_)
            #print("py:" + py)

    for app_ in config.APP_NAMES:
        dataframes = read_excel_sheets(file_path=config.INPUT_PATH_MODELS+ app_ + ".xlsx", sheet_names=config.sheet_names)
        for py in config.sheet_names: # Create a disctionnairy of dataframes for each .py file of teh django app
            if 'help' not in py:
                print("py: " + py)
                dataframes[py] = dataframes[py].dropna(subset="app_name")
                dataframes_py[app_][py] = dataframes[py]
        print("----------------app: " + app_)
    df_py_list = {}
    df_py = {}
    for py in config.sheet_names: # Create a disctionnairy of dataframes for each .py file of teh django app
        if 'help' not in py:
            df_py_list[py]=[]
            for app_ in config.APP_NAMES:
                df_py_list[py].append(dataframes_py[app_][py][~dataframes_py[app_][py].loc[:,py].isna()])  
        df_py[py] = pd.concat(df_py_list[py], ignore_index=True).reset_index()    
    # create list with models
    # create dataframes with appended dat across all xlsx files
            
    #print(df_py)
    return  df_py

def read_django_settings(file_name = config.INPUT_PATH_MODELS + "django-settings.pkl"):
# Later, you can load the dictionary back from the pickle file
    loaded_data = pd.read_pickle(file_name)
    return loaded_data

df_py = concatenate_py_files(config)
print(f"{df_py['model']['app_name'][df_py['model']['app_name'].isna()].count()}")

# Export the dictionary to a pickle file
pd.to_pickle(df_py, config.INPUT_PATH_MODELS + "django-settings.pkl")

print("---------")
print(read_django_settings(file_name = config.INPUT_PATH_MODELS + "django-settings.pkl"))
print(df_py['model'][~df_py['model'].loc[:,"app_name"].isna()])