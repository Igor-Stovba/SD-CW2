import pika

RABBITMQ_URL = 'amqp://localhost'

def setup_rabbitmq():
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()

    channel.queue_declare(queue='orders.worker')
    channel.queue_declare(queue='orders.server')
    channel.queue_declare(queue='feedback.worker')
    channel.queue_declare(queue='feedback.server')
    channel.queue_declare(queue='info.server')
    connection.close()