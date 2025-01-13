from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_user():
    """ 
        test hit endpoint user
        seharusnya memerlukan token, 
        sehinga kalau coba hit tanpa token 
        akan return status code 403
        dan message 'Not authenticated'
    """
    response = client.get("/user")
    assert response.status_code == 403
    assert response.json()["message"] == "Not authenticated"