import pika
import redis
import json
import os


redis_host = os.getenv("REDIS_HOST", "redis")
rabbitmq_host = os.getenv("RABBITMQ_HOST", "rabbitmq")

# Connexion à Redis
redis_client = redis.Redis(host=redis_host, port=6379, db=0)

# Connexion à RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()
channel.queue_declare(queue='calculator_queue', durable=True)

# Fonction pour effectuer un calcul
def perform_calculation(operation):
    try:
        num1, operator, num2 = operation
        num1, num2 = float(num1), float(num2)
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2 if num2 != 0 else 'Error: Division by zero'
        else:
            return 'Error: Invalid operator'
    except Exception as e:
        return f'Error: {str(e)}'

# Fonction pour consommer les messages RabbitMQ
def callback(ch, method, properties, body):
    data = json.loads(body)
    calc_id = data['id']
    operation = data['tuple']
    
    # Effectuer le calcul
    result = perform_calculation(operation)
    
    # Stocker le résultat dans Redis
    redis_client.set(calc_id, json.dumps({'status': 'done', 'result': result}))
    
    # Accuser réception du message
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Configurer le consommateur
channel.basic_consume(queue='calculator_queue', on_message_callback=callback)

print('Consommateur en attente des calculs...')
channel.start_consuming()
