#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_bnb():
    """Return "Hello, BNB!"""""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return "HBNB."""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Return text with C appended to it."""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python_text(text='is cool'):
    """Return text with Python appended to it."""
    return f"C {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def num_n(n):
    """Return n if its an integer"""
    if isinstance(n, int):
        return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
