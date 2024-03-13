# Heere we create the script for the producer of events for communicating across our microservices
import config

def basic_context(config, model_name):
    context = f"""
import pika
params = pika.URLParameters('{config.RABBITMQ_URL}')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == '{model_name.lower()}_created':
        {model_name.lower()} = {model_name}.objects.get(id=data['id'], title=data['title'], image=data['image']) # add more fields from the model
        db.session.add({model_name.lower()})
        db.session.commit()
        print('{model_name} created!')

    elif properties.content_type == '{model_name.lower()}_updated':
        {model_name.lower()} = {model_name}.objects.get(id=data['id']) # add more fields from the model
        {model_name.lower()}.title = data['title']
        {model_name.lower()}image = data['image']
        db.session.commit()
        print('{model_name} updated!')

    elif properties.content_type == '{model_name.lower()}_deleted':
        {model_name.lower()} = {model_name}.objects.get(data) # add more fields from the model
        db.session.delete({model_name.lower()})
        db.session.commit()
        print('{model_name} deleted!')
        

channel.basic_consume(queue='{config.FLASK_APP_MAIN_NAME}', on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()

"""
    return context
