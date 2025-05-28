import pika, json, sqlite3
from common import RABBITMQ_URL


def log_to_db(event_type, data):
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {event_type} (data) VALUES (?)", [json.dumps(data)])
    conn.commit()
    conn.close()


def on_message(channel, method, properties, body):
    data = json.loads(body)
    log_to_db(method.routing_key, data)
    print(f"Logged: {method.routing_key}")


def start_server():
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()

    channel.basic_consume(queue='order.worker', on_message_callback=on_message, auto_ack=True)
    channel.basic_consume(queue='feedback.worker', on_message_callback=on_message, auto_ack=True)
    channel.basic_consume(queue='maintenance.worker', on_message_callback=on_message, auto_ack=True)

    channel.start_consuming()


start_server()