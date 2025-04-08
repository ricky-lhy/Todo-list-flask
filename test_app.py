from app import app

def test_homepage():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'To-Do List' in response.data
        