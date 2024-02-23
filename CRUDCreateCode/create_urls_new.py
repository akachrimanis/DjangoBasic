import os
import config
import pandas as pd
def create_urls(df, model_name):

    # Starting script
    urls_content = f"""



    # {model_name.lower()}s
    path('', views.{model_name}ListView.as_view(), name='{model_name.lower()}-list'),
    path('create/', views.{model_name}CreateView.as_view(), name='{model_name.lower()}-create'),
    path('update/<int:pk>/', views.{model_name}UpdateView.as_view(), name='{model_name.lower()}-update'),
    path('delete/<int:pk>/', views.{model_name}DeleteView.as_view(), name='{model_name.lower()}-delete'),
    path('<int:pk>/', views.{model_name}ListView.as_view(), name='{model_name.lower()}-detail'),

"""
    return urls_content

def save_file_py(my_string, output_path, model_name, file_name="forms.py"):
    full_path = os.path.join(os.path.join(output_path,model_name), file_name)
    print(f"FILEPATH {file_name}: {full_path}")
# Writing the string to the file
    try:
        with open(full_path, 'x'):
            pass  # Do nothing if the file already exists
    except FileNotFoundError:
        print(f"File '{full_path}' does not exist")
    except FileExistsError:
        print(f"File '{full_path}' already exists")
        
    with open(full_path, 'w') as file:
        file.write(my_string + "\n")

    print(f"String has been saved to {full_path}")




def read_django_settings(file_name = config.INPUT_PATH_MODELS + "django-settings.pkl"):
# Later, you can load the dictionary back from the pickle file
    loaded_data = pd.read_pickle(file_name)
    return loaded_data

def find_model_names(df, column_name="model"):
    return loaded_data[column_name]["model_name"].unique()
def find_app_names(df, column_name="model"):
    return loaded_data[column_name]["app_name"].unique()
#print(find_model_names(loaded_data, column_name="model"))


loaded_data = read_django_settings(file_name = config.INPUT_PATH_MODELS + "django-settings.pkl")

#print(find_app_names(loaded_data, column_name="model"))
app_names = find_app_names(loaded_data, column_name="model")


app_model_content = {}
for app_name in app_names:
    content = f"""from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .forms import *
from . import views\n
router = DefaultRouter()\n"""
    content_include = f"""urlpatterns = [\n"""
    df = loaded_data['model']
    model_names = df[df["app_name"]==app_name]["model_name"].unique().tolist()
    content_form = ""
    print(f"---------{app_name}-------------")
    print("----------------------")

    print(f"{model_names}")
    content_routers = ""
    for model_name in model_names:
        content_routers += f"""router.register(r'{model_name.lower()}s', views.{model_name}ViewSet)\n"""
        content_form += create_urls(df, model_name)
    content +=  content_routers + content_include + content_form + f"""\n    path('api/1/', include(router.urls)),
    path('home/', views.home, name='home'),]"""    
    save_file_py(content, config.BASIC_APP_PATH, app_name, file_name="urls.py")
    
    #app_model_content[forms_content]