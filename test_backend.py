import requests
import json


# Test the backend directly
def test_backend():
    base_url = 'http://127.0.0.1:5000'

    # Test 1: Check if server is running
    try:
        response = requests.get(f'{base_url}/')
        print(f"1. Homepage status: {response.status_code}")
    except Exception as e:
        print(f"1. Cannot connect to server: {e}")
        return

    # Test 2: Test encryption endpoint
    try:
        test_data = {
            'text': 'hello',
            'algorithm': 'caesar'
        }
        response = requests.post(
            f'{base_url}/encrypt',
            json=test_data,
            headers={'Content-Type': 'application/json'}
        )
        print(f"2. Encrypt endpoint status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"2. Encrypt test failed: {e}")

    # Test 3: Test simple endpoint
    try:
        response = requests.get(f'{base_url}/test')
        print(f"3. Test endpoint: {response.json()}")
    except Exception as e:
        print(f"3. Test endpoint failed: {e}")


if __name__ == '__main__':
    test_backend()