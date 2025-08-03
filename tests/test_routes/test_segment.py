
data = [
    {'key': 'Segment A', 'name': 'seg 1', 'description': 'Test segment 1'},
    {'key': 'Segment B', 'name': 'seg 2', 'description': 'Test segment 2'}
]


def test_create_segment_route(client):
    response = client.post('/segments', json=data[0])
    assert response.status_code == 201
    assert response.json()['key'] == data[0]['key']


def test_get_segment_route(client):
    post = client.post('/segments', json=data[0])
    segment_id = post.json()['id']
    response = client.get(f'/segments/{segment_id}')
    assert response.status_code == 200
    assert response.json()['id'] == segment_id


def test_get_segments_route(client):
    client.post("/segments/", json=data[0])
    client.post("/segments/", json=data[1])
    response = client.get('/segments')
    assert response.status_code == 200
    segments = response.json()
    assert isinstance(segments, list)
    assert len(segments) == 2


def test_update_segment_route(client):
    post = client.post("/segments/", json=data[0])
    segment_id = post.json()['id']
    put = client.put(f"/segments/{segment_id}", json={"key": "New segment"})
    assert put.status_code == 200
    assert put.json()['key'] == 'New segment'


def test_delete_segment_route(client):
    post = client.post("/segments/", json=data[0])
    segment_id = post.json()['id']
    delete = client.delete(f'/segments/{segment_id}')
    nothing_response = client.get('/segments')
    assert delete.status_code == 204
    assert len(nothing_response.json()) == 0
