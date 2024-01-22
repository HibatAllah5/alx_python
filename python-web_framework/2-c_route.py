"""
 script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)

@app.route ('/' , strict_slashes=False)

def hello():
    """
    This function returns a simple string 'Hello HBNB!' when the root
    URL ('/') is accessed.
    
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def text1():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def text2(text):
    underscore = text.replace('_', ' ')
    return f'C {underscore}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)
