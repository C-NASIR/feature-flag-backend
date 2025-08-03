from uuid import uuid4
from datetime import datetime, timezone
from src.schemas.variation import (
    VariationCreate, VariationUpdate, VariationInDB
)


data = {'key': 'key a', 'value': 'value a',
        'description': 'nothing here'}


def test_variation_create_schema():
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
        'description': 'this is a description',
        'value': 'values',
        'flag_id': uuid4(),
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc)}
    variation = VariationInDB(**data)
    variation.key = 'key b'
