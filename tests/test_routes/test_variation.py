import pytest


@pytest.fixture
def var_data(flag_id):
    return [
        {'key': 'key 1', 'value': True, 'flag_id': flag_id},
        {'key': 'key 2', 'value': 'Lol', 'flag_id': flag_id}
    ]


def test_create_variation_route(client, var_data):
    post = client.post('/variations', json=var_data[0])

    assert post.status_code == 201
    assert post.json()['key'] == var_data[0]['key']


def test_get_variation_route(client, var_data):
    post = client.post('/variations', json=var_data[0])
    var_id = post.json()['id']
    resp = client.get(f'/variations/{var_id}')

    assert resp.status_code == 200
    assert resp.json()['key'] == var_data[0]['key']


def test_get_variations_route(client, var_data):
    client.post('/variations', json=var_data[0])
    client.post('/variations', json=var_data[1])
    resp = client.get(f'/variations')

    assert resp.status_code == 200
    assert len(resp.json()) == 2


def test_update_variation_route(client, var_data):
    post = client.post('/variations', json=var_data[0])
    id = post.json()['id']
    resp = client.put(f'/variations/{id}', json={'key': 'key B'})

    assert resp.status_code == 200
    assert resp.json()['key'] == 'key B'


def test_delete_variation_route(client, var_data):
    post = client.post('/variations', json=var_data[0])
    id = post.json()['id']
    resp = client.delete(f'/variations/{id}')

    assert resp.status_code == 200
    assert resp.json()['ok'] == True
