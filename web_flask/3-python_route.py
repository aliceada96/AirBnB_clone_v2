#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_bnb():
    """return "Hello, BNB!"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Return text + " is cool!"""""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python_text(text='is cool'):
    """Return text with Python appended to it."""
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
