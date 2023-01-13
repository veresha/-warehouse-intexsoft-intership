import os

from celery import Celery
from src.app.config import *

app = Celery(
    'worker',
    broker=RABBITMQ_BROKER,
    backend=RABBITMQ_BACKEND,
    include=['src.celery_app.tasks']
)
app.autodiscover_tasks()
