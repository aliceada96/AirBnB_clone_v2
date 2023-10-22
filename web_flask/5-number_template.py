#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask, render_template
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

@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """Return n if its an integer using template"""
    if isinstance(n, int):
        h1 = f"Number: {n}"
        return render_template('5-number.html', h1=h1)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
