import pika

RABBITMQ_URL = 'amqp://localhost'

def setup_rabbitmq():
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()

    # channel.exchange_declare(exchange='orders.direct', exchange_type='direct')
    # channel.exchange_declare(exchange='feedback.direct', exchange_type='direct')

    channel.queue_declare(queue='orders.worker')
    channel.queue_declare(queue="orders.server")
    # channel.queue_declare(queue='feedback.worker')

    # channel.queue_bind(exchange='orders.direct', queue='orders.worker', routing_key='orders.submitted')
    # channel.queue_bind(exchange='feedback.direct', queue='feedback.worker', routing_key='feedback.submitted')

    connection.close()