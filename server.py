import pika, json, sqlite3
from common import RABBITMQ_URL, setup_rabbitmq

conn = sqlite3.connect('events.db')
cursor = conn.cursor()

def log_to_db(event_type, data):
    table_name = event_type.split(".")[0]

    try:
        cursor.execute(f"INSERT INTO {table_name} (data) VALUES (?)", [json.dumps(data)])
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def on_message_orders(channel, method, properties, body):
    data = json.loads(body)
    log_to_db(method.routing_key, data)
    print(f"on_message_orders, Logged: {method.routing_key}")

def on_message_feedback(channel, method, properties, body):
    data = json.loads(body)
    log_to_db(method.routing_key, data)
    print(f"on_message_feedback, Logged: {method.routing_key}")

def on_message_info(channel, method, properties, body):
    data = json.loads(body)

    if (data['command'] == 'info'):
        cursor.execute("SELECT data FROM goods")
        rows = cursor.fetchall()

        goods_list = [json.loads(row[0]) for row in rows]
        channel.basic_publish(
            exchange='',
            routing_key='info.server',
            body=json.dumps(goods_list)
        )
    print(f"on_message_info, Logged: {method.routing_key}")

def start_server():
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()

    channel.basic_consume(queue='orders.server', on_message_callback=on_message_orders, auto_ack=True)
    channel.basic_consume(queue='feedback.server', on_message_callback=on_message_feedback, auto_ack=True)
    channel.basic_consume(queue='info.server', on_message_callback=on_message_info, auto_ack=True)
    channel.start_consuming()

setup_rabbitmq()
start_server()