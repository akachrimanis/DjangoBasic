# Heere we create the script for the producer of events for communicating across our microservices
import config

def basic_context(config, model_name):
    context = f"""
import pika, json, os, django
params = pika.URLParameters('{config.RABBITMQ_URL}')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='{config.FLASK_APP_MAIN_NAME}', body=json.dumps(body), properties=properties)
    connection.close()
"""
    return context
