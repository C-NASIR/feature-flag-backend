import pytest
from . import var_data


@pytest.fixture
def var_id(client, flag_id):
    response = client.post(f'/flags/{flag_id}/variations', json=var_data[0])
    return response.json()['id']


def test_get_variation_route(client, var_id):
    response = client.get(f'/variations/{var_id}')

    assert response.status_code == 200
    assert response.json()['key'] == var_data[0]['key']


def test_update_variation_route(client, var_id):
    resp = client.put(f'/variations/{var_id}', json={'key': 'key B'})

    assert resp.status_code == 200
    assert resp.json()['key'] == 'key B'


def test_delete_variation_route(client, var_id):
    resp = client.delete(f'/variations/{var_id}')

    assert resp.status_code == 200
    assert resp.json()['ok'] == True
