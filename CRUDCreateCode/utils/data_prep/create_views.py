def create_views(df, model_name):
    df = df.astype(str)

    # Starting script
    views_content = f"""from rest_framework import viewsets
from .models import {model_name.capitalize()}
from .serializers import {model_name.capitalize()}Serializer\n"""
    
    views_class = f"""\nclass {model_name.capitalize()}ViewSet(viewsets.ModelViewSet):
    queryset = {model_name.capitalize()}.objects.all()
    serializer_class = {model_name.capitalize()}Serializer
    """
    print(views_content + views_class)
    return views_content + views_class
