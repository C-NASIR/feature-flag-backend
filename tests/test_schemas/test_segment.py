from uuid import uuid4
from datetime import datetime, timezone
from src.schemas.segment import SegmentCreate, SegmentUpdate, SegmentInDB


def test_segment_create_schema():
    data = {'key': 'Segment A', 'name': 'seg 1', 'description': 'Test segment'}
    schema = SegmentCreate(**data)
    assert schema.key == 'Segment A'
    assert schema.description == 'Test segment'


def test_segment_update_schema():
    data = {'key': 'New Name'}
    schema = SegmentUpdate(**data)
    assert schema.key == 'New Name'
    assert schema.description is None


def test_segment_in_db_schema():
    now = datetime.now(timezone.utc)
    schema = SegmentInDB(
        id=uuid4(),
        key='Segment A',
        name='seg 1',
        description='Test',
        rule_segment_id=uuid4(),
        created_at=now,
        updated_at=now,
    )
    assert schema.key == 'Segment A'
    assert schema.created_at == now
