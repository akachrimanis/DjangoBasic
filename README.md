# DjangoBasic
This is a basic Django App used for  training, testing and iterating on ideas with colleagues of AIMONETIZE initiative

# TODO
- add signasls functionality in the CRUDCreateCode
- templates:chart templates in CRUDCreateCode
- url: add the charts
- views: add special vierws for serving:
  - dashboards
  - data presentations
  - charts
  - CRUD
  - SEARCH/ filtering etc
  - add sending coplex data and with field and meta information to athe api
- models: add aggregates with signal
  - aggregate in terms of time, variables, customer etc
  - add models for CRM 
  - add models for different tables for customer segments needs
  - add role based security
  - create fake data for the models and teh scripts to create them
  - create code to autpcreate multiple models per app. Fix teh code and the excel file. Add a column to all sheets with teh name of the model and on teh next column(s) will be their definitions
- charts:
  - create a UI for managing the colours, optinos, configurations etc of the charts.js
  - create functionality:
    - filters
    - selections
    - ranges
    - tickboxes
    - chart type
  - Add a set of chart templates of different types with combinations of colours and settings to choose from
- website-html:
  - fix the dashboard layout
  - fill in the dashboard layout with the dynamic charts
  - add the filters/ searches/ ranges etc accordingly
- react:
  - create a dashboard app
  - create the templates for a series of charts
  - create the api connection
- security
  ````
  Ensuring the security of your Django project is crucial for protecting sensitive data and preventing potential security breaches. Here are some of the most important security configurations to assess and implement:

1. **SECRET_KEY Protection**:
   - Keep your `SECRET_KEY` value secure and avoid exposing it in version control or publicly accessible locations.
   - Store your `SECRET_KEY` in an environment variable or a separate configuration file that is not publicly accessible.

   ```python
   # settings.py
   SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
   ```

2. **DEBUG Mode**:
   - Disable the `DEBUG` mode in production to prevent detailed error messages from being displayed to users, which can expose sensitive information.

   ```python
   # settings.py
   DEBUG = False
   ```

3. **Allowed Hosts**:
   - Define a list of allowed hosts in your Django settings to prevent HTTP Host header attacks.

   ```python
   # settings.py
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

4. **HTTPS Configuration**:
   - Use HTTPS to encrypt data transmitted between the client and the server, especially for sensitive information such as authentication credentials.
   - Configure your web server (e.g., Nginx, Apache) to enforce HTTPS and redirect HTTP requests to HTTPS.

5. **CSRF Protection**:
   - Enable CSRF protection to prevent Cross-Site Request Forgery attacks.

   ```python
   # settings.py
   CSRF_COOKIE_SECURE = True
   ```

6. **X-Frame-Options Header**:
   - Set the `X-Frame-Options` header to prevent your site from being embedded in frames on other domains, which can help mitigate Clickjacking attacks.

   ```python
   # settings.py
   X_FRAME_OPTIONS = 'DENY'
   ```

7. **Content Security Policy (CSP)**:
   - Implement a Content Security Policy to control which resources are allowed to be loaded by your web application, reducing the risk of XSS attacks.

   ```python
   # settings.py
   CSP_DEFAULT_SRC = ("'self'",)
   ```

8. **Authentication and Authorization**:
   - Use Django's built-in authentication system for user authentication and authorization.
   - Implement proper access controls to restrict users' permissions based on their roles and privileges.

9. **Password Management**:
   - Enforce strong password policies, such as minimum length and complexity requirements.
   - Use Django's password hashing mechanism to securely store user passwords.

10. **Regular Security Updates**:
    - Keep Django and its dependencies up-to-date with the latest security patches to address known vulnerabilities.

11. **Input Validation and Sanitization**:
    - Validate and sanitize user inputs to prevent injection attacks (e.g., SQL injection, XSS).
    - Use Django's built-in form validation and model field validation to validate user inputs.

12. **Secure File Uploads**:
    - Implement proper validation and restrictions on file uploads to prevent malicious files from being uploaded to your server.
    - Store uploaded files in a secure location with restricted access.

By implementing these security configurations and best practices, you can enhance the security posture of your Django project and reduce the risk of potential security threats. Additionally, regularly conducting security audits and vulnerability assessments can help identify and address any security weaknesses in your application.
  ````

- add django channels and asynchronous communication with websockets
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
pip install pandas openpyxl numpy jupyterlab django-simple-history
pip install celery django-debug-toolbar django-allauth django-cors-headers django-filter django-crispy-forms djangorestframework-simplejwt
pip install channels redis # asynchronous/ websockets
pip install openai
pip install scrapy
pip install redis celery  

# flask app requirements
pip install flask requests SQLAlchemy pika Flask-Migrate mysqlclient Flask-Cors Flask-Scripts 
pip install -U Flask-SQLAlchemy
pip install -U flask-cors

django-admin startproject backend
python3 manage.py startapp Customer
python3 manage.py migrate
python3 manage.py createsuperuser
user=tkax
password=test1234!

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

# Create project with prefilled stuff
python3 /Users/tkax/dev/aimonetize/Backend/DjangoBasic/CRUDCreateCode/main.py



python3 manage.py startapp Organisation Product CustomerB2B CustomerB2C Dashdoard CRM EventTracking

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
  - create text for the models.py
  - create the folder structure - run the createapp script for teh specific model and teh folder structure is created automatically
  - copy the boilerplate files accordingly
    - style.css
    - settings.py
    - urls.py
  - Create the necessary files (if not existing)
    - forms.py
    - urls.py
    - serializers.py
    - signals.py -TODO
    - celery.py -TODO
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


### admin



### serializers
Serializers is a straightforward function that peety much stays teh same across the models


### signals



### html



### charts



# Docker install + Celery
[Building a Django Docker Container](https://www.youtube.com/watch?v=PkynrL1aU9o&list=PLOLrQ9Pn6cayGytG1fgUPEsUp3Onol8V7&index=3)

````
chmod +x ./entrypoint.sh
docker-compose up -d --build 
./ manage.py start app taskapp
docker exec -it django /bin/sh
./ manage.py start app cworker

````

- Create the celery structure and files either as an app within teh django project or as a standalone app
- create task routing
- cretae task prioritization
- celery task grouping
- celery task chaining
- celery task rate limits