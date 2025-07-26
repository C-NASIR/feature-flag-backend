from uuid import uuid4
from datetime import datetime, timezone
from src.schemas.variation import (
    VariationCreate, VariationUpdate, VariationInDB
)


def test_variation_create_schema():
    data = {'key': 'key a', 'flag_id': uuid4(), 'value': 'values'}
    variation = VariationCreate(**data)
    variation.key = 'key a'


def test_variation_update_schema():
    data = {'key': 'key b'}
    variation = VariationUpdate(**data)
    variation.key = 'key b'


def test_variation_in_db_schema():
    data = {
        'id': uuid4(),
        'key': 'key a',
        'flag_id': uuid4(),
        'value': 'values',
        'flag_id': uuid4(),
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc)}
    variation = VariationUpdate(**data)
    variation.key = 'key b'
