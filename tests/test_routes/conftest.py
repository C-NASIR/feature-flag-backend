import pytest
from . import flag_data, env_data, rule_data


@pytest.fixture
def flag_id(client):
    resp_env = client.post('/environments', json=env_data[0])
    env_id = resp_env.json()['id']

    resp = client.post(f'/environments/{env_id}/flags', json=flag_data[0])
    return resp.json()['id']


@pytest.fixture
def rule_id(client, flag_id):
    response = client.post(f'/flags/{flag_id}/rules', json=rule_data[0])
    return response.json()['id']
