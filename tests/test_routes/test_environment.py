from . import flag_data, env_data


# Env route tests
def test_create_env_route(client):
    response = client.post('/environments', json=env_data[0])
    assert response.status_code == 201
    assert response.json()['name'] == env_data[0]['name']


def test_get_env_route(client):
    post = client.post('/environments', json=env_data[0])
    env_id = post.json()['id']
    response = client.get(f'/environments/{env_id}')
    assert response.status_code == 200
    assert response.json()['id'] == env_id


def test_get_envs_route(client):
    client.post("/environments", json=env_data[0])
    client.post("/environments", json=env_data[1])
    response = client.get('/environments')
    assert response.status_code == 200
    envs = response.json()
    assert isinstance(envs, list)
    assert len(envs) == 2


def test_update_env_route(client):
    post = client.post('/environments', json=env_data[0])
    env_id = post.json()['id']
    put = client.put(f"/environments/{env_id}", json={"name": "New env"})
    assert put.status_code == 200
    assert put.json()['name'] == 'New env'


def test_delete_env_route(client):
    post = client.post('/environments', json=env_data[0])
    env_id = post.json()['id']
    delete = client.delete(f'/environments/{env_id}')
    nothing_response = client.get('/environments')
    assert delete.status_code == 200
    assert len(nothing_response.json()) == 0


# Flag Route Tests
def test_create_flag_route(client):
    response = client.post('/environments', json=env_data[0])
    env_id = response.json()['id']
    response = client.post(f'/environments/{env_id}/flags', json=flag_data[0])
    assert response.status_code == 201
    assert response.json()['key'] == flag_data[0]['key']


def test_get_flags_route(client):
    response = client.post('/environments', json=env_data[0])
    env_id = response.json()['id']

    client.post(f'/environments/{env_id}/flags', json=flag_data[0])
    client.post(f'/environments/{env_id}/flags', json=flag_data[1])

    response = client.get(f'/environments/{env_id}/flags')
    assert response.status_code == 200
    assert len(response.json()) == 2
