import pytest


@pytest.fixture
def env_id(client):
    response = client.post('/environments', json={'name': 'env 1'})
    return response.json()['id']


@pytest.fixture
def flag_id(client, env_id):
    data = {'key': "flag-a",
            'name': "Flag A",
            'environment_id': env_id,
            'description': "Enables Flag A",
            'default_variation': "on",
            'enabled': True}

    response = client.post('/flags', json=data)
    return response.json()['id']
