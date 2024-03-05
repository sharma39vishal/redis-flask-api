from flask import Flask, jsonify, request
import redis
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to Redis Cloud
redis_host = os.environ['REDIS_HOST']
redis_port = os.environ['REDIS_PORT']
redis_password = os.environ['REDIS_PASSWORD']

# Create a connection to Redis
r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Initialize Flask app
app = Flask(__name__)

# API endpoint to get the value associated with a key
@app.route('/get_value/<key>', methods=['GET'])
def get_value(key):
    value = r.get(key)
    if value is not None:
        return jsonify({'key': key, 'value': value}), 200
    else:
        return jsonify({'error': 'Key not found'}), 404

# API endpoint to set a key-value pair
@app.route('/set_value', methods=['POST'])
def set_value():
    data = request.json
    if 'key' in data and 'value' in data:
        key = data['key']
        value = data['value']
        r.set(key, value)
        return jsonify({'message': 'Key-value pair set successfully'}), 201
    else:
        return jsonify({'error': 'Key and value must be provided in JSON format'}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
