from tasks import add

result = add.delay(5,5)


# Everytime this file get called
# it will execute the tasks listed 
# add.delay(10,5)