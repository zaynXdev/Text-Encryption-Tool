import json
import urllib.request
import urllib.parse


def test_backend_simple():
    base_url = 'http://127.0.0.1:5000'

    print("Testing Backend Connection...")

    # Test 1: Check if server is running
    try:
        with urllib.request.urlopen(f'{base_url}/') as response:
            print(f"✅ 1. Homepage status: {response.status}")
    except Exception as e:
        print(f"❌ 1. Cannot connect to server: {e}")
        return

    # Test 2: Test health endpoint
    try:
        with urllib.request.urlopen(f'{base_url}/health') as response:
            data = json.loads(response.read().decode())
            print(f"✅ 2. Health check: {data}")
    except Exception as e:
        print(f"❌ 2. Health check failed: {e}")

    # Test 3: Test encryption endpoint
    try:
        test_data = {
            'text': 'hello',
            'algorithm': 'caesar'
        }

        # Convert data to JSON bytes
        json_data = json.dumps(test_data).encode('utf-8')

        # Create request
        req = urllib.request.Request(
            f'{base_url}/encrypt',
            data=json_data,
            headers={'Content-Type': 'application/json'}
        )

        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print(f"✅ 3. Encrypt endpoint: {data}")

    except Exception as e:
        print(f"❌ 3. Encrypt test failed: {e}")


if __name__ == '__main__':
    test_backend_simple()