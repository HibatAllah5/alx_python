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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)
