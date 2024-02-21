def create_apps(model_name, df, config):
    context = f"""from django.apps import AppConfig
class {model_name}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{model_name}'"""
    return context



