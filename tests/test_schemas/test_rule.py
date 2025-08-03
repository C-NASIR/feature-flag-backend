from uuid import uuid4
from datetime import datetime, timezone
from src.schemas.rule import RuleCreate, RuleUpdate, RuleInDB


def test_rule_create_schema():
    data = {'variation': 'on', 'priority': 3, 'conditions': []}
    schema = RuleCreate(**data)

    assert schema.variation == data['variation']
    assert schema.priority == data['priority']


def test_rule_update_schema():
    schema = RuleUpdate(variation='off')

    assert schema.variation == 'off'


def test_rule_response_schema():
    data = {
        'id': uuid4(),
        'variation': 'off',
        'priority': 3,
        'conditions': [],
        'flag_id': uuid4(),
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc)
    }

    schema = RuleInDB(**data)

    assert schema.variation == data['variation']
    assert schema.priority == data['priority']
    assert isinstance(schema.created_at, datetime)
