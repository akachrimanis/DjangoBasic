
from utils.dataIO.read_model_xlsx import *
#import config
import os
import config
print(os.getcwd())
print(config.INPUT_PATH_MODELS)


#print(dataframes["model"])

#create a new table structure
# - table name
# primary key/ foreignkey
def create_dbdiagram(dataframes, config):
    df_models = dataframes["model"].sort_values("model_name")
    model_names = df_models["model_name"].unique()
    print(model_names)
    table_component = ""
    reference_component = ""
    model_ = ""
    PRIMARY_KEY = 'id'
    count_ = 0  
    #table_component
    for i in df_models.index:
        #print(df_models.loc[i,"Variable"])
        CURRENT_VARIABLE = df_models.loc[i,"Variable"]
        CURRENT_VARTYPE = df_models.loc[i,"Type"].replace("models.","").replace("Field","")
        #print(df_models.loc[i,"model_name"])
        CURRENT_MODEL_NAME = df_models.loc[i,"model_name"]
        #NEXT_MODEL_NAME = df_models.loc[min(df_models["Variable"].shape[0],i+1),"model_name"]

        # FK_table is the name of teh foreign key table
        FK_table = df_models.loc[i,"Args"].replace("models.","").replace("Field","")
        if 'primary_key=True' in df_models.loc[i,"Args"]:
            PRIMARY_KEY = df_models.loc[i,"Variable"]
        if model_ != CURRENT_MODEL_NAME:
            table_component += f"""\n
            """
            if count_> 1:
                table_component += f"}}\n"

            table_component += f"table {CURRENT_MODEL_NAME} {{\n"
            if 'primary_key=True' not in df_models.loc[i,"Args"]:
                table_component += f"\t\tid integer [primary key] \n"
            table_component += f"\t\t{CURRENT_VARIABLE} {CURRENT_VARTYPE}\n"
            if 'primary_key=True' in df_models.loc[i,"Args"]:
                table_component += f"\t\t{CURRENT_VARIABLE} {CURRENT_VARTYPE}"
                table_component += f" integer [primary key]\n"
                
        else:
            table_component += f"\t\t{CURRENT_VARIABLE} {CURRENT_VARTYPE}\n"
                    
        
        model_ = CURRENT_MODEL_NAME
        if CURRENT_VARTYPE in ["ForeignKey", "OneToOne", "OneToMany", "ManyToMany"]:
            #print(FK_table[FK_table.find("(")+1:FK_table.find(",")])
            s= FK_table[FK_table.find("(")+1:FK_table.find(",")]
            if 'self' in s:
                s = CURRENT_MODEL_NAME.split(".")[-1]
            if  "'" in s:
                s = s.replace("'","")
            reference_component += f"Ref: {CURRENT_MODEL_NAME}.{CURRENT_VARIABLE} > {s}.{PRIMARY_KEY} \n"
        count_ += 1

    table_component += f"\n\t\t}}"
    #print(table_component)
    #print("--" - FK_table)
    #print(reference_component)
    content = table_component + "\n" + reference_component
    return content, df_models


def list_sheets_xlsx(file_path, config):
    import openpyxl

    for app_ in config.APP_NAMES:
        print(f"--------------{app_}----------------")

        # Load the workbook
        workbook = openpyxl.load_workbook(file_path + app_ + ".xlsx")

        # Get the sheet names
        workbook.close()
list_sheets_xlsx(file_path=config.INPUT_PATH_MODELS, config=config)
content = ""
df_append_list = []






for app_ in config.APP_NAMES:

    dataframes = read_excel_sheets(file_path=config.INPUT_PATH_MODELS+ app_ + ".xlsx", sheet_names=config.sheet_names)
   
    print(f"--------------{app_}----------------")
    content += create_dbdiagram(dataframes, config)[0] + "\n"
    df_append_list.append(create_dbdiagram(dataframes, config)[1])

df_append=pd.concat(df_append_list)
df_append = df_append.sort_values("model_name")
def save_dbdiagram_content(my_string, output_path,):
    file_name = "dbdiagram.txt"
    full_path = os.path.join(output_path, file_name)
    print(f"FILEPATH {file_name}: {full_path}")
# Writing the string to the file
    with open(full_path, 'w') as file:
        file.write(my_string + "\n")

    print(f"String has been saved to {full_path}")

content += f"""\ntable User {{
    id integer [primary key]
}}"""

save_dbdiagram_content(content, output_path=config.INPUT_PATH_MODELS)
print("-----------------------------------------------")
print("-----------------------------------------------")
print("-----------------------------------------------")

print(df_append)         

# Save DataFrame to an Excel file
df_append.to_excel(config.INPUT_PATH_MODELS + 'all_data_models.xlsx', index=False)  # Set index=False to exclude the DataFrame index from the Excel file
df_append.to_pickle(config.INPUT_PATH_MODELS + "all_data_models.pickle")


