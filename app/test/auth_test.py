from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_content():
    """ 
        test login dengan username & password yang disediakan 
        seharusnya return status code 200
        dan memiliki data 'access_token'
    """
    response = client.post("/token", data={"username": "admin", "password": "password"})
    assert response.status_code == 200 
    assert 'access_token' in response.json()["data"]
