import pika, json
from common import RABBITMQ_URL

def on_order(channel, method, properties, body):
    order = json.loads(body)
    print(f"order id: {order['id']}, items: {order['items']}")


connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
channel = connection.channel()

channel.basic_consume(queue='orders.worker', on_message_callback=on_order, auto_ack=True)
channel.start_consuming()
