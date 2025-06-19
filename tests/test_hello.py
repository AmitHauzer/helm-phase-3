import requests
import time
import pytest
import subprocess

URL_MESSAGE: str = "Hello, World!!!!!"


@pytest.mark.docker
def test_flask_app_responds():
    # Optional wait if the app starts slowly
    time.sleep(1)
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200
    assert response.text.strip() == URL_MESSAGE


@pytest.mark.kubernetes
def test_flask_app_responds_via_kubernetes():
    # This test assumes that the Flask app is running in a Kubernetes cluster
    # and that the service is accessible via the specified URL.
    # Replace with the actual service URL if needed.

    time.sleep(1)
    NODE_PORT: str = subprocess.check_output(
        ["kubectl", "get", "--namespace", "default", "-o", 'jsonpath={.spec.ports[0].nodePort}', "services", "test-app-amitchart"], text=True).strip()
    NODE_IP: str = subprocess.check_output(["kubectl", "get", "nodes", "--namespace", "default",
                                           "-o", 'jsonpath={.items[0].status.addresses[0].address}'], text=True).strip()
    URL: str = f"http://{NODE_IP}:{NODE_PORT}/"
    print(f"Testing Flask app at: {URL}")

    response = requests.get(URL)
    assert response.status_code == 200
    assert response.text.strip() == URL_MESSAGE
