import requests
import time


def test_flask_app_responds():
    # Optional wait if the app starts slowly
    time.sleep(1)
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200
    assert response.text.strip() == "Hello, World!"
