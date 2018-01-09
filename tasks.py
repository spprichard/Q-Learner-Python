from celery import Celery
from testqlearner import test_code

rabbit = 'amqp://guest@localhost:5672//'
app = Celery('tasks', backend=rabbit, broker=rabbit)


@app.task
def add(x, y):
    return x + y

@app.task
def learner():
    return test_code()