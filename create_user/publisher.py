import sys
import pika

def publisher(message):
    connection= pika.BlockingConnection(
            pika.ConnectionParameters(host='192.168.219.1'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    
    channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2, # make message persistent
            ))
    
    print(" [x] Sent %r" % message)
    connection.close()
    return "ok"

if __name__ == '__main__':
    message= "".join(sys.argv[1:]) or "Hello World!"
    publisher(message)


