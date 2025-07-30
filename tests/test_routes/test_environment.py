
data = [
    {"key": "key 1", "name": "dev"},
    {"key": "key 2", "name": "prod"}
]


def test_create_env_route(client):
    response = client.post('/environments', json=data[0])
    assert response.status_code == 201
    assert response.json()['name'] == data[0]['name']


def test_get_env_route(client):
    post = client.post('/environments', json=data[0])
    env_id = post.json()['id']
    response = client.get(f'/environments/{env_id}')
    assert response.status_code == 200
    assert response.json()['id'] == env_id


def test_get_envs_route(client):
    client.post("/environments", json=data[0])
    client.post("/environments", json=data[1])
    response = client.get('/environments')
    assert response.status_code == 200
    envs = response.json()
    assert isinstance(envs, list)
    assert len(envs) == 2


def test_update_env_route(client):
    post = client.post('/environments', json=data[0])
    env_id = post.json()['id']
    put = client.put(f"/environments/{env_id}", json={"name": "New env"})
    assert put.status_code == 200
    assert put.json()['name'] == 'New env'


def test_delete_env_route(client):
    post = client.post('/environments', json=data[0])
    env_id = post.json()['id']
    delete = client.delete(f'/environments/{env_id}')
    nothing_response = client.get('/environments')
    assert delete.status_code == 200
    assert len(nothing_response.json()) == 0
