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
@main.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        'message': 'This is a GET request',
        'timestamp': datetime.utcnow().isoformat()
    })

# API Route 2: POST Endpoint (handles JSON data)
@main.route('/api/data', methods=['POST'])
def post_data():
    if not request.is_json:
        return jsonify({"error": "Invalid input, JSON expected"}), 400

    data = request.get_json()
    return jsonify({
        'data': data,
        'timestamp': datetime.utcnow().isoformat()
    })