import pika, json
from common import RABBITMQ_URL

def send_event(event_type, data):
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()
    
    if event_type == 'orders':
        print('a')
        channel.basic_publish(
            exchange='',
            routing_key='orders.worker',
            body=json.dumps(data)
        )
        channel.basic_publish(
            exchange='',
            routing_key='orders.server',
            body=json.dumps(data)
        )
    elif event_type == 'feedback':
        channel.basic_publish(
            exchange='feedback.direct',
            routing_key='feedback.submitted',
            body=json.dumps(data)
        )
    
    connection.close()

send_event('orders', {'id': 123, 'items': ['coffee', 'cake'], 'status': 'submitted'})
send_event('feedback', {'id': 123, 'items': ['coffee', 'cake'], 'status': 'submitted'})
