from testqlearner import test_code
from app import app
import time

@app.task
def add(x, y):
    return x + y

@app.task
def long_add(x, y): 
    time.sleep(5)
    return x + y

# @app.task
# def learner():
#     return test_code()