
def test_create_segment_route(client):
    data = {'key': 'Segment 1', 'description': 'desc'}
    response = client.post('/segments', json=data)
    assert response.status_code == 201
    assert response.json()['key'] == 'Segment 1'


def test_get_segment_route(client):
    data = {'key': 'Segment 2', 'description': 'desc'}
    post = client.post('/segments', json=data)
    segment_id = post.json()['id']
    response = client.get(f'/segments/{segment_id}')
    assert response.status_code == 200
    assert response.json()['id'] == segment_id


def test_get_segments_route(client):
    client.post("/segments/", json={"key": "Segment 1"})
    client.post("/segments/", json={"key": "Segment 2"})
    response = client.get('/segments')
    assert response.status_code == 200
    segments = response.json()
    assert isinstance(segments, list)
    assert len(segments) == 2


def test_update_segment_route(client):
    post = client.post("/segments/", json={"key": "Old segment"})
    segment_id = post.json()['id']
    put = client.put(f"/segments/{segment_id}", json={"key": "New segment"})
    assert put.status_code == 200
    assert put.json()['key'] == 'New segment'


def test_delete_segment_route(client):
    post = client.post("/segments/", json={"key": "Delete Segment"})
    segment_id = post.json()['id']
    delete = client.delete(f'/segments/{segment_id}')
    nothing_response = client.get('/segments')
    assert delete.status_code == 204
    assert len(nothing_response.json()) == 0
