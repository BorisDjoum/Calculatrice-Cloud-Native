from flask import Flask, send_from_directory, jsonify, request
import redis
import pika
import uuid
import json
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
rabbitmq_host = os.getenv("RABBITMQ_HOST", "rabbitmq")

# Connexion à Redis
redis_client = redis.Redis(host=redis_host, port=6379, db=0)



connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()
channel.queue_declare(queue='calculator_queue', durable=True)

# Générer un ID unique
def generate_id():
    return str(uuid.uuid4())

# Route pour servir le fichier `index.html`
@app.route('/')
def serve_frontend():
    # Chemin absolu vers le dossier frontend
    frontend_path = os.path.join(os.path.dirname(__file__), '../frontend')
    return send_from_directory(frontend_path, 'index.html')

# API : Calculatrice (POST pour envoyer un calcul)
@app.route('/api/v1/calcul', methods=['POST'])
def create_calculation():
    data = request.json
    if not data or 'tuple' not in data:
        return jsonify({'error': 'Invalid data, expected {"tuple": [number1, operator, number2]}'})
    
    calc_id = generate_id()
    operation = data['tuple']
    redis_client.set(calc_id, json.dumps({'status': 'pending', 'result': None}))
    channel.basic_publish(
        exchange='',
        routing_key='calculator_queue',
        body=json.dumps({'id': calc_id, 'tuple': operation}),
        properties=pika.BasicProperties(delivery_mode=2)
    )
    return jsonify({'id': calc_id}), 201

# API : Récupérer le résultat d'un calcul
@app.route('/api/v1/calcul/<calc_id>', methods=['GET'])
def get_calculation(calc_id):
    calc_data = redis_client.get(calc_id)
    if not calc_data:
        return jsonify({'error': 'Calculation not found'}), 404
    return jsonify(json.loads(calc_data)), 200

@app.route('/test_redis')
def test_redis():
    try:
        redis_client.ping()  # Vérifie si Redis répond
        return jsonify({'status': 'Redis is running'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Lancer Flask sur le port 5000
    app.run(host='127.0.0.1', port=5000, debug=True)
    