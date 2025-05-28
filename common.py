
import pika

RABBITMQ_URL = 'amqp://localhost'

def setup_rabbitmq():
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()

    channel.exchange_declare(exchange='orders.direct', exchange_type='direct')
    channel.exchange_declare(exchange='info.fanout', exchange_type='fanout')
    channel.exchange_declare(exchange='feedback.direct', exchange_type='direct')
    channel.exchange_declare(exchange='maintenance.topic', exchange_type='topic')

    channel.queue_declare(queue='order.worker')
    channel.queue_declare(queue='feedback.worker')
    channel.queue_declare(queue='maintenance.worker')

    channel.queue_bind(exchange='orders.direct', queue='order.worker', routing_key='order.submitted')
    channel.queue_bind(exchange='feedback.direct', queue='feedback.worker', routing_key='feedback.submitted')
    channel.queue_bind(exchange='maintenance.topic', queue='maintenance.worker', routing_key='maintenance.request')

    connection.close()
