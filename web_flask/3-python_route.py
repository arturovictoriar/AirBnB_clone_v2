"""
    Start a Flask web application on 0.0.0.0, port 5000
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    """Say Hello HBNB to the client"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    """Say HBNB to the client"""
    return 'HBNB'


@app.route('/c/<text>')
def c_isfun(text):
    """Say C and a given text to the client"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_iscool(text='is cool'):
    """Say Python and a given text to the client"""
    return 'Python {}'.format(text.replace('_', ' '))

app.run(host='0.0.0.0', port=5000)
