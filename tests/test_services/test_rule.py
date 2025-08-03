from src.schemas.rule import RuleCreate, RuleUpdate
from src.services.rule_service import (
    get_rules, get_rule, create_rule, update_rule, delete_rule
)


data = [
    {'variation': 'on', 'priority': 3, 'conditions': []},
    {'variation': 'off', 'priority': 2, 'conditions': []}
]


def test_create_rule(db_session, flag_id):
    rule_data = RuleCreate(**data[0])
    rule = create_rule(db_session, flag_id, rule_data)
    assert rule.variation == data[0]['variation']
    assert rule.priority == data[0]['priority']


def test_get_rule(db_session, flag_id):
    rule_data = RuleCreate(**data[0])
    created = create_rule(db_session, flag_id, rule_data)
    rule = get_rule(db_session, created.id)

    assert rule.variation == data[0]['variation']
    assert rule.priority == data[0]['priority']


def test_get_rules(db_session, flag_id):
    rule_data1 = RuleCreate(**data[0])
    rule_data2 = RuleCreate(**data[1])
    create_rule(db_session, flag_id, rule_data1)
    create_rule(db_session, flag_id, rule_data2)

    assert len(get_rules(db_session)) == 2


def test_update_rule(db_session, flag_id):
    rule_data = RuleCreate(**data[0])
    created = create_rule(db_session, flag_id, rule_data)
    updated_data = RuleUpdate(variation='updated var')
    updated = update_rule(db_session, created.id, updated_data)

    assert created.id == updated.id
    assert created.priority == updated.priority
    assert updated.variation == 'updated var'


def test_delete_rule(db_session, flag_id):
    rule_data = RuleCreate(**data[0])
    created = create_rule(db_session, flag_id, rule_data)
    deleted = delete_rule(db_session, created.id)
    assert deleted['ok'] == True
    assert len(get_rules(db_session)) == 0
