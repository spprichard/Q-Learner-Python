import pika
import time


def main():    
    send("hello from main")
    time.sleep(10)
    receive()
    return 0
    
def receive():
    # Connect to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    # Declare queue that we will be consuming from
    channel.queue_declare(queue='default')

    channel.basic_consume(callback, queue='default', no_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    

def callback(channel, method, properties, body):
    print "[X] received message"
    print "message: \n"
    print body

    


    

def send(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='default')

    channel.basic_publish(exchange='', routing_key='default', body=message)
    print(" [x] Sent '" + message + "'")

    connection.close()


if __name__ == '__main__':
    main()