from uuid import uuid4
from datetime import datetime, timezone
from src.schemas.condition import ConditionCreate, ConditionUpdate, ConditionInDB


def test_condition_create_schema():
    data = {'attribute': 'email', 'operator': '=', 'value': 'val 1'}
    schema = ConditionCreate(**data)
    assert schema.attribute == data['attribute']
    assert schema.operator == data['operator']


def test_condition_update_schema():
    schema = ConditionUpdate(operator='>')
    assert schema.operator == '>'


def test_condition_in_db_schema():
    now = datetime.now(timezone.utc)
    schema = ConditionInDB(
        id=uuid4(),
        attribute='name',
        operator='<',
        value='Test',
        rule_id=uuid4(),
        created_at=now,
        updated_at=now,
    )
    assert schema.attribute == 'name'
    assert schema.created_at == now
