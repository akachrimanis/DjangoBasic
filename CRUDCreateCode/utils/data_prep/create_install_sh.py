def create_install_sh(df):
    content = f"""
    
#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Apply Django migrations
python manage.py migrate
    
    """
    return content
