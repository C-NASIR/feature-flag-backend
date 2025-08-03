import pytest
from . import condition_data


@pytest.fixture
def condition_id(client, rule_id):
    response = client.post(
        f'/rules/{rule_id}/conditions', json=condition_data[0])
    return response.json()['id']


def test_get_condition_route(client, condition_id):
    response = client.get(f'/conditions/{condition_id}')

    assert response.status_code == 200
    assert response.json()['attribute'] == condition_data[0]['attribute']


def test_update_condition_route(client, condition_id):
    resp = client.put(f'/conditions/{condition_id}', json={'operator': '='})

    assert resp.status_code == 200
    assert resp.json()['operator'] == '='


def test_delete_condition_route(client, condition_id):
    resp = client.delete(f'/conditions/{condition_id}')

    assert resp.status_code == 200
    assert resp.json()['ok'] == True
