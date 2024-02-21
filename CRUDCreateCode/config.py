import os

sheet_names = ['model','model_functions', 'serializers', 'views', 'html', 'forms', "urls", "admin"]# "apps", "imports"
parameter_vars = ['ForeignKey', 'through', 'parent_link', 'related_name', 'related_query_name', 'on_delete', 'primary_key', 'max_length', 'unique', 'blank', 'null', 'default', 'auto_now_add', 'auto_now','verbose_name']
APP_NAMES= ['Organisation','CustomerB2B', 'CustomerB2C', 'Dashboard','Product', 'EventTracking', 'UserProfile', "CRM"]
name_staticfiles = "mystaticfiles"
name_media_folder = "media"
MAIN_APP_NAME = 'backend'
BASIC_APP_PATH = os.path.join(os.getcwd(),f"{MAIN_APP_NAME}") # backend
BACKEND_MAINAPP_PATH = os.path.join(os.getcwd(),f"{MAIN_APP_NAME}/{MAIN_APP_NAME}") # backend/backend


BASIC_PATH = os.path.join(os.getcwd(),"CRUDCreateCode") # create template script
template_mystaticfiles_PATH = os.path.join(BASIC_PATH,"utils/templates/mystaticfiles")

MAIN_APP_mystaticfiles_PATH = os.path.join(BASIC_APP_PATH,name_staticfiles)
MAIN_APP_media_PATH = os.path.join(BASIC_APP_PATH,name_media_folder) # media
MAIN_APP_templates_PATH = os.path.join(BASIC_APP_PATH,"templates") # templates

INPUT_PATH_SETTINGS = os.path.join(BASIC_PATH, "data/input/settings/")
INPUT_PATH_MODELS = os.path.join(BASIC_PATH, "data/input/models/")

#css
# DESTINATION_FOLDER_CSS = os.path.join(BASIC_PATH,"style.css")
DESTINATION_FOLDER_CSS = os.path.join(MAIN_APP_mystaticfiles_PATH,"style.css")
SOURCE_FOLDER_CSS = os.path.join(template_mystaticfiles_PATH,"style.css")


# settings.py
SETTINGS_FILENAME = "settings.xlsx"
SOURCE_FOLDER_SETTINGS = os.path.join(BASIC_PATH,"utils/templates")


# models.copy()    
