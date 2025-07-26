
def get_flag_data(env_id):
    return [
        {'key': "flag-a",
            'name': "Flag A",
            'environment_id': env_id,
            'description': "Enables Flag A",
            'default_variation': "on",
            'enabled': True},
        {'key': "flag-b",
         'name': "Flag B",
         'environment_id': env_id,
         'description': "Enables Flag B",
         'default_variation': "on",
         'enabled': False}
    ]


def test_create_flag_route(client, env_id):
    flags_data = get_flag_data(env_id)
    response = client.post('/flags', json=flags_data[0])
    assert response.status_code == 201
    assert response.json()['name'] == 'Flag A'


def test_get_flag_route(client, env_id):
    flags_data = get_flag_data(env_id)
    post = client.post('/flags', json=flags_data[0])
    flag_id = post.json()['id']
    response = client.get(f'/flags/{flag_id}')
    assert response.status_code == 200
    assert response.json()['id'] == flag_id
    assert response.json()['name'] == 'Flag A'


def test_get_flags_route(client, env_id):
    flags_data = get_flag_data(env_id)
    client.post("/flags", json=flags_data[0])
    client.post("/flags", json=flags_data[1])
    response = client.get('/flags')
    assert response.status_code == 200
    flags = response.json()
    assert isinstance(flags, list)
    assert len(flags) == 2


def test_update_flag_route(client, env_id):
    flags_data = get_flag_data(env_id)
    post = client.post('/flags', json=flags_data[1])
    flag_id = post.json()['id']
    put = client.put(f"/flags/{flag_id}", json={"name": "New flag"})
    assert put.status_code == 200
    assert put.json()['name'] == 'New flag'


def test_delete_flag_route(client, env_id):
    flags_data = get_flag_data(env_id)
    post = client.post('/flags', json=flags_data[1])
    flag_id = post.json()['id']
    delete = client.delete(f'/flags/{flag_id}')
    nothing_response = client.get('/flags')
    assert delete.status_code == 200
    assert len(nothing_response.json()) == 0
