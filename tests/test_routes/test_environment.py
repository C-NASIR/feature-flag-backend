

def test_create_env_route(client):
    response = client.post('/environments', json={'name': 'env 1'})
    assert response.status_code == 201
    assert response.json()['name'] == 'env 1'


def test_get_env_route(client):
    data = {'name': 'env 2'}
    post = client.post('/environments', json=data)
    env_id = post.json()['id']
    response = client.get(f'/environments/{env_id}')
    assert response.status_code == 200
    assert response.json()['id'] == env_id


def test_get_envs_route(client):
    client.post("/environments", json={"name": "env 1"})
    client.post("/environments", json={"name": "env 2"})
    response = client.get('/environments')
    assert response.status_code == 200
    envs = response.json()
    assert isinstance(envs, list)
    assert len(envs) == 2


def test_update_env_route(client):
    post = client.post('/environments', json={'name': 'new env'})
    env_id = post.json()['id']
    put = client.put(f"/environments/{env_id}", json={"name": "New env"})
    assert put.status_code == 200
    assert put.json()['name'] == 'New env'


def test_delete_env_route(client):
    post = client.post('/environments', json={'name': 'to delete'})
    env_id = post.json()['id']
    delete = client.delete(f'/environments/{env_id}')
    nothing_response = client.get('/environments')
    assert delete.status_code == 200
    assert len(nothing_response.json()) == 0
