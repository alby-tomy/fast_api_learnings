from fastapi.testclient import TestClient
import main
from fastapi import status

client = TestClient(main.app)

def test_return_object():
    response = client.get("/healthy")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "API is healthy"}