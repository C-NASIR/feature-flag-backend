from . import rule_data, condition_data


def test_get_rule_route(client, rule_id):
    response = client.get(f'/rules/{rule_id}')

    assert response.status_code == 200
    assert response.json()['variation'] == rule_data[0]['variation']


def test_update_rule_route(client, rule_id):
    resp = client.put(f'/rules/{rule_id}', json={'priority': 5})

    assert resp.status_code == 200
    assert resp.json()['priority'] == 5


def test_delete_rule_route(client, rule_id):
    resp = client.delete(f'/rules/{rule_id}')

    assert resp.status_code == 200
    assert resp.json()['ok'] == True


# Condition Route Tests
def test_create_condition_route(client, rule_id):
    response = client.post(
        f'/rules/{rule_id}/conditions', json=condition_data[0])
    assert response.status_code == 201
    assert response.json()['attribute'] == condition_data[0]['attribute']


def test_get_conditions_route(client, rule_id):
    client.post(f'/rules/{rule_id}/conditions', json=condition_data[0])
    client.post(f'/rules/{rule_id}/conditions', json=condition_data[0])
    response = client.get(f'/rules/{rule_id}/conditions')
    assert response.status_code == 200
    assert (len(response.json())) == 2
