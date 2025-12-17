import requests

# Contstant for API url
API_URL = "https://jsonplaceholder.typicode.com"

# Simple test to confirm that API can be reached 
def test_api_is_reachable():
    response = requests.get(API_URL)
    assert response.status_code == 200

# Test to get user and confirm data 
def test_get_user():
    endpoint = f"{API_URL}/users/1"
    response = requests.get(endpoint)

    # Confirm that endpoint can be reached
    assert response.status_code == 200
    
    # Parse the JSON data
    data = response.json()
    
    # Check that data is present
    assert data['id'] == 1
    assert data['name'] == "Leanne Graham"
    assert 'email' in data
    assert 'phone' in data
    # assert 'lastname' in data