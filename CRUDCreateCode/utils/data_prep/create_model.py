
def create_model(df, model_name):
    df = df.astype(str)
    df["max_length"] = df["max_length"].apply(lambda x: x[:-2] if x != "nan" else "nan")
    print(" The dataframe is:")
    print(df)
    print("\n The columns of model sheet are: ")
    print(df.columns.tolist())
    
    print("\n The model's variables are:")
    print(df[df["filter_use"] == "True"]["Variable"].tolist())
    
    
    df = df[df["filter_use"] == "True"]
    
    # Starting script
    model_content = f"""from django.db import models

# Create your models here.
class {model_name}(models.Model):\n"""
    
    # create a list with all teh field types in the model variables
    variable_types=df["Type"].unique()
    # create teh text for importing teh libraries of teh fieldtypes
    fieldtypes_libraries = """from django.db.models import ("""
    for i in variable_types:
        fieldtypes_libraries += f"{i},"
    fieldtypes_libraries = fieldtypes_libraries[:-1] + ")\n\n"
    print(variable_types)
    # add the variables with their parameters
    parameter_vars = ['ForeignKey', 'through', 'parent_link', 'related_name', 'related_query_name', 'on_delete', 'primary_key', 'max_length', 'unique', 'blank', 'null', 'default', 'auto_now_add', 'auto_now']
    model_definitions = ""
    for i in df.index:
        var_name = df.loc[i, "Variable"]
        type_name = df.loc[i, "Type"] 
        model_variable_definition = f"    {var_name} = {type_name}("
        for p in  parameter_vars:
            param_context=df.loc[i, p]
            if param_context == "1.0":
                param_context = True
            if param_context == "0.0":
                param_context = False
            if str(param_context) !=  "nan":
                model_variable_definition += f"{p}={param_context},"
        model_variable_definition += "),\n"
        model_definitions += model_variable_definition
    model_definitions = fieldtypes_libraries + model_content + model_definitions
    return model_definitions 

# add extra functionality
def create_functionality(df):
    model_functionality = ""
    for i in df.index:
        function_text = df.loc[i,"functions"]
        model_functionality += f"""{function_text}\n\n"""

    return model_functionality