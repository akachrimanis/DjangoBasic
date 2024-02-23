import os
import config
import pandas as pd
import pickle

# Assuming your pickled file is named 'data.pkl'
with open(f'{config.INPUT_PATH_MODELS}all_data_models.pickle', 'rb') as f:
    df = pickle.load(f)

model_names = df['model_name'].unique()
all_types = df['Type'].unique()

print(f"These are the models: \n{model_names}")
print(f"These are the types: \n{all_types}")

for model_ in model_names:
    # keep 
    CURRENT_MODEL_NAME = model_
    df_model = df[df['model_name']==CURRENT_MODEL_NAME]
    print("CURRENT_MODEL_NAME: " + CURRENT_MODEL_NAME)
    print(df_model.columns)