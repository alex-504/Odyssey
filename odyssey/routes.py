from flask import Blueprint, render_template, jsonify, request
from datetime import datetime

# Define the blueprint
main = Blueprint('main', __name__)

# HTML Route 1: Home Page
@main.route('/')
def home():
    return render_template('home.html')  # Ensure 'home.html' exists in templates

# HTML Route 2: About Page
@main.route('/about')
def about():
    return render_template('about.html')  # Ensure 'about.html' exists in templates

# API Route 1: GET Endpoint (returns JSON data)
import requests

@main.route('/api/data', methods=['GET'])
def get_data():
    response = requests.get('https://official-joke-api.appspot.com/jokes/programming/random')
    joke = response.json()[0]

    return jsonify({
        'message 1': "This is a GET Request",
        'message': f"{joke['setup']} {joke['punchline']}",
        'timestamp': datetime.utcnow().isoformat()
    })

# API Route 2: POST Endpoint (handles JSON data)
# POST route that accepts data from the URL (query parameters)
# POST route that accepts query parameters
@main.route('/api/data', methods=['POST'])
def post_data():
    name = request.form.get('name')
    age = request.form.get('age')

    if not name or not name.isalpha():
        return jsonify({"error": "Invalid or missing name"}), 400

    if not age or not age.isdigit():
        return jsonify({"error": "Invalid or missing age"}), 400

    return jsonify({
        'name': name,
        'age': age,
        'timestamp': datetime.utcnow().isoformat()
    })