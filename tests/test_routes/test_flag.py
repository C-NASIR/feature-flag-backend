from . import var_data, rule_data


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


# Variation Route Tests
def test_create_variation_route(client, flag_id):
    response = client.post(f'/flags/{flag_id}/variations', json=var_data[0])
    assert response.status_code == 201
    assert response.json()['key'] == var_data[0]['key']


def test_get_variations_route(client, flag_id):
    client.post(f'/flags/{flag_id}/variations', json=var_data[0])
    client.post(f'/flags/{flag_id}/variations', json=var_data[1])

    response = client.get(f'/flags/{flag_id}/variations')
    assert response.status_code == 200
    assert (len(response.json())) == 2

# Rules Route Tests


def test_create_rule_route(client, flag_id):
    response = client.post(f'/flags/{flag_id}/rules', json=rule_data[0])
    assert response.status_code == 201
    assert response.json()['variation'] == rule_data[0]['variation']


def test_get_rules_route(client, flag_id):
    client.post(f'/flags/{flag_id}/rules', json=rule_data[0])
    client.post(f'/flags/{flag_id}/rules', json=rule_data[1])

    response = client.get(f'/flags/{flag_id}/rules')
    assert response.status_code == 200
    assert (len(response.json())) == 2
