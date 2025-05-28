
import pika, json
from common import RABBITMQ_URL

def send_event(event_type, data):
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()
    
    if event_type == 'order':
        channel.basic_publish(
            exchange='orders.direct',
            routing_key='order.submitted',
            body=json.dumps(data)
        )
    elif event_type == 'feedback':
        channel.basic_publish(
            exchange='feedback.direct',
            routing_key='feedback.submitted',
            body=json.dumps(data)
        )
    
    connection.close()

send_event('order', {'id': 123, 'items': ['coffee', 'cake'], 'status': 'submitted'})
