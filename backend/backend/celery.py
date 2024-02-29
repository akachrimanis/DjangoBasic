import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
app = Celery("backend")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.task_routes = {'CustomerB2B.tasks.task1':{'queue':'queue1'}, 'CustomerB2B.tasks.task2':{'queue':'queue2'}}
# Crete tasks  for Celery
@app.task
def add_numbers():
    return 

# app.config.broker_transport_options = {
#     'priority_steps': list(range(10)),
#     'sep':':',
#     'queue_order_strategy':'priority',
# }
app.autodiscover_tasks()