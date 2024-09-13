import requests
import json

# URL of your Flask API POST endpoint
url = 'http://localhost:5001/api/data'

# Data to send in the POST request
data = {
    "name": "John Doe",
    "age": 30
}

# Send the POST request with JSON data
response = requests.post(url, json=data)

# Print the raw response and status code to see what the server returned
print("Status Code:", response.status_code)
print("Response Text:", response.text)

# Attempt to parse the response as JSON, if it returns JSON
try:
    print("Response JSON:", response.json())
except requests.exceptions.JSONDecodeError:
    print("Response is not valid JSON")