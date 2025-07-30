import pytest
from . import flag_data, env_data


@pytest.fixture
def flag_id(client):
    resp_env = client.post('/environments', json=env_data[0])
    env_id = resp_env.json()['id']

    resp = client.post(f'/environments/{env_id}/flags', json=flag_data[0])
    return resp.json()['id']


def test_get_flag_route(client, flag_id):
    response = client.get(f'/flags/{flag_id}')
    assert response.status_code == 200
    assert response.json()['id'] == flag_id
    assert response.json()['name'] == 'Flag A'


def test_update_flag_route(client, flag_id):
    put = client.put(f"/flags/{flag_id}", json={"name": "New flag"})
    assert put.status_code == 200
    assert put.json()['name'] == 'New flag'


def test_delete_flag_route(client, flag_id):
    delete = client.delete(f'/flags/{flag_id}')
    assert delete.status_code == 200
