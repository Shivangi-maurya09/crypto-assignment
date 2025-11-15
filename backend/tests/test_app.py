import sys
import os

# Add backend folder to system path FORCEFULLY
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app   # now Python will find app.py inside backend/

def test_ping():
    client = app.test_client()
    response = client.get("/ping")
    assert response.status_code == 200

def test_price():
    client = app.test_client()
    response = client.get("/price?symbol=BTC")
    assert response.status_code == 200
