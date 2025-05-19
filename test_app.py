from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"DevOps" in response.data  # Adjust to match your actual output
