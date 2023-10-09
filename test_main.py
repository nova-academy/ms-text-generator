"""Importing modules"""
from fastapi.testclient import TestClient
from main import app
from mock import patch

client = TestClient(app=app)


@patch('openai.ChatCompletion.create')
def test_generate_text(mock_openai):
    """Returns 200"""
    mock_openai.return_value = {
        "choices": [{
            'message': {
                'content': 'Generated Poem'
            }
        }]
    }

    response = client.post("/api/v1/text-generator",
                           json={'prompt': 'naturaleza'})
    assert response.status_code == 200
    assert response.json() == {'text': 'Generated Poem'}

# You need to create more test cases

# END
