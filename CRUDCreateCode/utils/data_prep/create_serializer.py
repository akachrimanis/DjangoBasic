def create_serializer(df, model_name):
    df = df.astype(str)


    # Starting script
    serializer_content = f"""from rest_framework import serializers\nfrom .models import {model_name}\n"""
    print(model_name.capitalize())

    serializer_class = f"""\nclass {model_name.capitalize()}Serializer(serializers.ModelSerializer):\n
    class Meta:
        model = {model_name}
        fields = "__all__"
        """
        
    return serializer_content + serializer_class

