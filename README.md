# DjangoBasic
This is a basic Django App used for  training, testing and iterating on ideas with colleagues of AIMONETIZE initiative


# Overview
The structure of this app is:
- Basic software installation
  - Install python 11
  - Install virtual environment
  - 
- CRUDCreateCode: is the code that creates automatically the:
  - models
  - views
  - urls
  - settings
  - admin
  - serializers
  - signals
  - celery
  - forms
  - html
    - basic html page(s)
    - API_frontend: create html pages that will be able to make the CRUD API possible
  - folder creation and structure
    - MEDIA
    - templates
    - 
  - runs the installation: assuming python and basic software is installed properly)
    - myenv: virtual environment
    - install python libraries with pip

## Basic software installation
### OSX

venv
````commandline
# run in command line
python3 -m venv myenv
source myenv/bin/activate
````
````commandline
# run in command line
# add environment in PATH
nano ~/.zshrc    
export PATH="/Users/tkax/dev/aimonetize/DjangoBasic/myenv/bin:$PATH"
````

````commandline
pip install --upgrade pip
pip install django djangorestframework
pip install pandas openpyxl numpy jupyterlab
pip install Pillow celery redis django-debug-toolbar django-allauth django-cors-headers django-filter django-crispy-forms djangorestframework-simplejwt

django-admin startproject backend
python3 manage.py startapp testapp
python3 manage.py migrate
python3 manage.py createsuperuser
user=tkax
password=test1234!

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

# Create project with prefilled stuff
python3 /Users/tkax/dev/aimonetize/Backend/DjangoBasic/CRUDCreateCode/main.py
````

## CRUDCreateCode

This source code is created to assist us in thecreation of boilerplate django backend frameworks in a robust, consistent and fast manner. The code provides an easy way to define your models and basic functionality of the views, serializers, etc and create automatically a ready to play django app wthat will corespond to teh info you inserted. it takes away the straggle and time-consuming effort to write connect the ORM framework as well provides out-of-the-box settings, structure and other fundamentls taht just take too much time to write again and again.
The steps to follow to achieve that are the following:

- Defive your models
  - Create one model_name.xlsx file for each model and save it in data/input/models. in each of the tabs add teh following information to alter the code accordingly. Follow the instructions on the template. Save teh file  under the data/input/models folder. the name of the file should be the same as the model name.
    - model structure and parameters definition
    - Serializers: model and parameters
    - views
    - urls
    - admin
    - forms
    - signal
- Create one settings.xlsx file following the xlsx template
- Run the settings script
  - Read the settings template
  - Assign variables
  - Create text for teh setting.py file
  - Write settings file
- Run the model script: 
  - Read the model template file for each model. 
  - transform the xls file into pandas dataframe
  - assign variables accordingly for all parameters
  - create text for the model
  - create the folder structure - run the createapp script for teh specific model and teh folder structure is created automatically
  - Create the necessary files (if not existing)
    - forms.py
    - urls.py
    - serializers.py
    - signals.py
    - celery.py
  - add model into settings.py
  - add configuration of router in urls(the main url in the main app folder backend/urls.py)
  - Make migrations

### Models


### views



### urls



### settings
When working with Django projects, there are several common libraries and packages that are often used to enhance functionality, improve development efficiency, and solve typical web development problems. Here's a list of some of the most commonly used libraries in Django projects:

1. **Django REST framework**: A powerful and flexible toolkit for building Web APIs. It's essential for projects where you need to create a RESTful API.

2. **Pillow**: A fork of PIL (Python Imaging Library) and is required for adding image processing capabilities to your Django application, especially if you're using `ImageField` in your models.

3. **Celery**: Used for asynchronous task processing. It allows you to run time-consuming tasks in the background, such as sending emails or processing large data.

4. **Redis**: Often used as a backend for caching and Celery. It's a high-performance key-value store that can speed up your site by caching pages, API calls, or data.

5. **Django Debug Toolbar**: A configurable set of panels that display various debug information about the current request/response and when developing locally.

6. **Django Allauth**: Provides authentication, registration, and account management. It supports both traditional username/password logins as well as social authentication.

7. **django-cors-headers**: A Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS). Essential for APIs consumed by web frontends hosted on different domains.

8. **django-filter**: A convenient library for filtering querysets from URL parameters, particularly useful for REST APIs.

9. **django-crispy-forms**: Helps to manage Django forms and render them in a DRY, clean, and elegant way. It's particularly useful for rendering forms in a template with minimal code.

10. **djangorestframework-simplejwt**: Provides a JSON Web Token Authentication backend for the Django REST Framework. It's a good choice for token-based authentication.

11. **gunicorn** or **uwsgi**: WSGI HTTP Servers for UNIX, used for deploying Django in production environments.

12. **psycopg2** or **mysqlclient**: Database adapters for PostgreSQL and MySQL, respectively. You'll need these if you're using one of these databases.

13. **django-extensions**: Provides a range of additional management commands and features for the Django Admin.

14. **django-compressor**: Compresses CSS and JavaScript files to improve load times.

15. **Whitenoise**: Simplifies the process of serving static files in production.

Remember, the libraries you choose should be based on the specific needs of your project. Always ensure compatibility with the Django version you are using and keep an eye on the maintenance status and community support for third-party libraries.

````python
"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import django
django.setup()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bm)sn&2^=4%(5b22s$w_fxcz$+t_50r3_-!2&(_l9p&rsdvk-a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #'Customer',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'crispy_forms',
    'corsheaders',
    'debug_toolbar',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.account.auth_backends.AuthenticationBackend',
    'index.apps.IndexConfig',
    'account.apps.AccountConfig',
    'community.apps.CommunityConfig',
    'django_filters',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# If STATICFILES_DIRS is not defined, add it
STATICFILES_DIRS = [
    BASE_DIR / 'mystaticfiles',  # Adjust the path to match your structure
]
# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

````

### admin



### serializers


### signals



### serializers



### serializers



