import pika, json, sqlite3
from common import RABBITMQ_URL, setup_rabbitmq

def log_to_db(event_type, data):
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()

    table_name = {
        'orders.submitted': 'orders',
        'feedback.submitted': 'feedbacks'
    }.get(event_type, 'unknown_events')

    try:
        cursor.execute(f"INSERT INTO {table_name} (data) VALUES (?)", [json.dumps(data)])
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def on_message(channel, method, properties, body):
    print('b')
    data = json.loads(body)
    log_to_db(method.routing_key, data)
    print(f"Logged: {method.routing_key}")


def start_server():
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()

    channel.basic_consume(queue='orders.worker', on_message_callback=on_message, auto_ack=True)
    channel.basic_consume(queue='feedback.worker', on_message_callback=on_message, auto_ack=True)
    channel.basic_consume(queue='maintenance.worker', on_message_callback=on_message, auto_ack=True)

    channel.start_consuming()

setup_rabbitmq()
start_server()