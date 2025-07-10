# app.py This is sample python progra
from flask import Flask

# Create a Flask web app instance
app = Flask(__name__)

@app.route('/')
def home():
    """This is the main page of the web application."""
    return "Hello, World! This is my first Jenkins CI/CD project."

if __name__ == '__main__':
    # This allows running the app directly for local testing
    # It will be accessible at http://127.0.0.1:5000
    app.run(host='0.0.0.0', port=5000)
