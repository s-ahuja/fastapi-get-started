import os

if os.path.isfile("bookstore.db"):
    print("removing sqllite database file")
    os.remove("bookstore.db")

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"message": "able to reach out to the test method"}
