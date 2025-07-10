# test_app.py
import pytest
from app import app as flask_app # Import the app from our app.py file

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_home_page(client):
    """
    Tests the main page ('/') of the application.
    It checks if the page loads successfully (status code 200)
    and if it contains the expected "Hello, World!" text.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data
