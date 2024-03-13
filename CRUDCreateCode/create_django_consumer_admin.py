# Heere we create the script for the producer of events for communicating across our microservices
import config

def basic_context(config, model_name):
    context = f"""
import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from {model_name}.models import {model_name}

params = pika.URLParameters('{config.RABBITMQ_URL}')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in main')
    id = json.loads(body)
    print(id)

    {model_name.lower()} = {model_name}.objects.get(id=id) # add more fields from the model
    {model_name.lower()}.likes = {model_name.lower()}.likes + 1
    {model_name.lower()}.save()
    print('Product likes increased!') 

        

channel.basic_consume(queue='{config.FLASK_APP_MAIN_NAME}', on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()

"""
    return context
