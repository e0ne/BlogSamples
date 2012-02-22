import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print body

channel.basic_consume(callback,
    queue='hello')

channel.start_consuming()
