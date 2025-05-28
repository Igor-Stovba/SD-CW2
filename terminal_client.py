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
            exchange='',
            routing_key='feedback.worker',
            body=json.dumps(data)
        )
        channel.basic_publish(
            exchange='',
            routing_key='feedback.server',
            body=json.dumps(data)
        )
    
    connection.close()

send_event('orders', {'id': 123, 'items': ['coffee', 'cake'], 'status': 'submitted'})
send_event('feedback', {'id': 123, 'items': ['coffee', 'cake'], 'status': 'submitted'})



while True:
    try:
        event_type = input("Введите тип события (orders/info/feedback/exit): ").strip()
        if event_type.lower() == 'exit':
            break

        data = []
        if event_type == 'orders':
            print("Для завершения ввода заказа введите 'end'")
            item = input("Введите товар: ").strip()

            while item != 'end':
                count = int(input("Введите количество: ").strip())
                item = input("Введите товар: ").strip()
                data.append({item: count})

        if event_type == 'feedback':
            message = input("Введите сообщение: ").strip()
            data.append(message)

        try:
            send_event(event_type, data)
            print(f"Событие успешно отправлено: {event_type} с данными {data}")
        except Exception as e:
            print(f"Ошибка: {str(e)}")

    except KeyboardInterrupt:
        print("\nПрограмма завершена")
        break

