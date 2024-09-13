import pytest
from odyssey import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

# Test GET request
def test_get_data(client):
    response = client.get('/api/data')
    assert response.status_code == 200
    json_data = response.get_json()
    assert "message" in json_data  # Check if 'message' exists
    assert "timestamp" in json_data  # Check if 'timestamp' exists

# Test POST request
def test_post_data(client):
    response = client.post('/api/data', data={'name': 'JohnDoe', 'age': '30'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert "name" in json_data  # Check if 'name' exists
    assert "age" in json_data  # Check if 'age' exists

# Test POST request for valid data
def test_post_data_valid(client):
    response = client.post('/api/data', data={'name': 'JohnDoe', 'age': '30'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert "name" in json_data
    assert "age" in json_data
    assert isinstance(json_data['name'], str)
    assert isinstance(json_data['age'], str)

# Test POST request with invalid data (name as a number)
def test_post_data_invalid_name(client):
    response = client.post('/api/data', data={'name': '12345', 'age': '30'})
    assert response.status_code == 400
    json_data = response.get_json()
    assert "error" in json_data
    assert json_data['error'] == "Invalid or missing name"

# Test POST request with invalid data (age as a string)
def test_post_data_invalid_age(client):
    response = client.post('/api/data', data={'name': 'JohnDoe', 'age': 'abc'})
    assert response.status_code == 400
    json_data = response.get_json()
    assert "error" in json_data
    assert json_data['error'] == "Invalid or missing age"

# Test POST request with missing data
def test_post_data_missing_fields(client):
    response = client.post('/api/data', data={})
    assert response.status_code == 400
    json_data = response.get_json()
    assert "error" in json_data
    assert json_data['error'] == "Invalid or missing name"