from src.schemas.condition import (
    ConditionCreate, ConditionUpdate
)
from src.services.condition_service import (
    get_conditions, get_condition, create_condition,
    update_condition, delete_condition
)


data = [
    {'attribute': 'email', 'operator': '=', 'value': 'var 1'},
    {'attribute': 'name', 'operator': '<', 'value': 'val 2'}
]


def test_create_condition(db_session, rule_id):
    rule_data = ConditionCreate(**data[0])
    condition = create_condition(db_session, rule_id, rule_data)
    assert condition.attribute == data[0]['attribute']
    assert condition.operator == data[0]['operator']


def test_get_condition(db_session, rule_id):
    rule_data = ConditionCreate(**data[0])
    created = create_condition(db_session, rule_id, rule_data)
    condition = get_condition(db_session, created.id)

    assert condition.attribute == data[0]['attribute']
    assert condition.operator == data[0]['operator']


def test_get_conditions(db_session, rule_id):
    rule_data1 = ConditionCreate(**data[0])
    rule_data2 = ConditionCreate(**data[1])
    create_condition(db_session, rule_id, rule_data1)
    create_condition(db_session, rule_id, rule_data2)

    assert len(get_conditions(db_session)) == 2


def test_update_condition(db_session, rule_id):
    rule_data = ConditionCreate(**data[0])
    created = create_condition(db_session, rule_id, rule_data)
    updated_data = ConditionUpdate(operator='<')
    updated = update_condition(db_session, created.id, updated_data)

    assert created.id == updated.id
    assert created.attribute == data[0]['attribute']
    assert updated.operator == '<'


def test_delete_condition(db_session, rule_id):
    rule_data = ConditionCreate(**data[0])
    created = create_condition(db_session, rule_id, rule_data)
    deleted = delete_condition(db_session, created.id)
    assert deleted['ok'] == True
    assert len(get_conditions(db_session)) == 0
