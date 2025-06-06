# Информационная система для торгового центра на RabbitMQ

## Описание системы

Система предназначена для обработки обращений посетителей торгового центра через терминалы, включая:
- Оформление и отмену заказов
- Информационные запросы (информацию о цене)
- Обратную связь 

## Компоненты системы

1. **Терминалы** - генерируют события от посетителей
2. **Сервер обработки** - принимает и логирует все события
3. **Клиенты сотрудников** - получают уведомления о новых событиях
4. **RabbitMQ** - брокер сообщений для обмена данными
5. **База данных SQLite** - хранит историю всех обращений

## Установка и настройка

### Предварительные требования
- Python 3.7+
- RabbitMQ сервер
- SQLite3

### Установка зависимостей
```bash
pip install pika
```

### Настройка RabbitMQ
Запустить RabbitMQ сервер

### Инициализация базы данных
```bash
sqlite3 events.db < init_db.sql
```

## Запуск системы

1. **Сервер обработки** 
```bash
python server.py
```

2. **Клиент терминала** 
```bash
python terminal_client.py
```

3. **Клиент сотрудника** (в отдельном терминале для каждого типа сотрудника):
```bash
# Для обработки заказов:
python worker_client.py 

# Для обработки обратной связи:
python worker_client.py 


```

## Структура базы данных

Система создает 3 таблицы:
1. `orders` - все заказы (включая отмененные)
2. `goods` - товары
3. `feedback` - обратная связь от посетителей


Каждая таблица содержит поля:
- `id` - первичный ключ
- `data` - JSON с полными данными события

## Мониторинг

Для мониторинга очередей RabbitMQ можно использовать:
1. Веб-интерфейс RabbitMQ (доступен по умолчанию на порту 15672)
2. Командная утилита `rabbitmqctl`

Пример проверки очередей:
```bash
rabbitmqctl list_queues
```

## Лицензия

MIT License
