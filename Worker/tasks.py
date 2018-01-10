from __future__ import absolute_import
from app import app
import time

@app.task
def add(x, y):
    return x + y

@app.task
def long_add(x, y): 
    print "long add starts"
    time.sleep(5)
    print "long add ends"
    return x + y