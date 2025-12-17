import requests

def test_api_is_reachable():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200