from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_content():
    """ 
        test hit endpoint content
        seharusnya tidak perlu token, 
        sehinga return status code 200
        dan memiliki data 'title' & 'slug'
    """
    response = client.get("/content")
    assert response.status_code == 200
    assert 'title' in response.json()["data"][0]
    assert 'slug' in response.json()["data"][0]