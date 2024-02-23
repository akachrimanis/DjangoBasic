# get model names
#get apps
import config
import  os
import pandas as pd

def read_django_settings(file_name = config.INPUT_PATH_MODELS + "django-settings.pkl"):
# Later, you can load the dictionary back from the pickle file
    loaded_data = pd.read_pickle(file_name)
    return loaded_data
            

def create_file_if_not_exists(filename):
    try:
        with open(filename, 'x'):
            pass  # Do nothing if the file already exists
    except FileExistsError:
        print(f"File '{filename}' already exists")


loaded_data = read_django_settings(file_name = config.INPUT_PATH_MODELS + "django-settings.pkl")
#print(loaded_data["model"])
def find_model_names(df, column_name="model"):
    return loaded_data[column_name]["model_name"].unique()
def find_app_names(df, column_name="model"):
    return loaded_data[column_name]["app_name"].unique()
def create_views(df, model_name):
    # Starting script
   
    
    views_class = f"""\n
class {model_name}ViewSet(viewsets.ModelViewSet):
    queryset = {model_name}.objects.all()
    serializer_class = {model_name}Serializer
    
     # {model_name} Views  
class {model_name}ListView(ListView):
    model = {model_name}
    template_name = '{model_name.lower()}-list.html'
    context_object_name = '{model_name.lower()}s'
    
class {model_name}DetailView(DetailView):
    model = {model_name}
    template_name = '{model_name.lower()}-details.html'
    context_object_name = '{model_name.lower()}s'

class {model_name}CreateView(CreateView):
    model = {model_name}
    form_class = {model_name}Form
    template_name = '{model_name.lower()}-form.html'
    success_url = reverse_lazy('{model_name.lower()}-list')  # Redirect to the CRUD view after successful creation

class {model_name}UpdateView(UpdateView):
    model = {model_name}
    form_class = {model_name}Form
    template_name = '{model_name.lower()}-form.html'
    success_url = reverse_lazy('{model_name.lower()}-list')  # Redirect to the CRUD view after successful update

class {model_name}DeleteView(DeleteView):
    model = {model_name}
    template_name = '{model_name.lower()}-confirm-delete.html'
    success_url = reverse_lazy('{model_name.lower()}-list')  # Redirect to the CRUD view after successful deletion
   
    """
    #print(views_content + views_class)
    return views_class

def save_views_py(my_string, output_path, model_name):
    file_name = "views.py"
    full_path = os.path.join(os.path.join(output_path,model_name), file_name)
    print(f"FILEPATH {file_name}: {full_path}")
# Writing the string to the file
    with open(full_path, 'w') as file:
        file.write(my_string + "\n")

    print(f"String has been saved to {full_path}")
    
    
#print(find_model_names(loaded_data, column_name="model"))
model_names = find_model_names(loaded_data, column_name="model")
#print(find_app_names(loaded_data, column_name="model"))
app_names = find_app_names(loaded_data, column_name="model")


app_model_content = {}
for app_name in app_names:
    df = loaded_data['model'][loaded_data['model']["app_name"]==app_name]
    views_main_imports = f"""from rest_framework import viewsets
from rest_framework import generics
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

def home(request):
    return render(request, "home.html",{{}})

"""
    views_imports = ""
    views_content = ""
    model_names = loaded_data['model'][loaded_data['model']["app_name"]==app_name]["model_name"].unique().tolist()
    
    serializer_models = f"\nfrom .serializers import"
    forms_models = f"\nfrom .forms import" 
    import_models = f"""\nfrom .models import"""

    print(model_names)
    for model_name in model_names:
        import_models += f""" {model_name},"""
        forms_models += f" {model_name}Form,"
        serializer_models += f" {model_name}Serializer,"
        views_content += create_views(df=df, model_name=model_name)
    app_model_content[app_name] = views_main_imports + import_models[:-1] + forms_models[:-1] + serializer_models[:-1] + views_content
    save_views_py(app_model_content[app_name], config.BASIC_APP_PATH, app_name)