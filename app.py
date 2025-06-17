"""Flask Hello World app"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """Return Hello World"""
    return "Hello, World!"
