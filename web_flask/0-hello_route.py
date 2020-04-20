"""
    Start a Flask web application on 0.0.0.0, port 5000
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    """Say hello to the client"""
    return 'Hello HBNB!'

app.run(host='0.0.0.0', port=5000)
