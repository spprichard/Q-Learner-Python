from __future__ import absolute_import
from celery import Celery

rabbit = 'amqp://guest@localhost:5672//'
app = Celery('qlearn', backend=rabbit, broker=rabbit)
