from src.models.segment import Segment
from src.schemas.segment import SegmentCreate, SegmentUpdate
from src.services.segment_service import (
    get_segments, get_segment, create_segment,
    update_segment, delete_segment
)

data = [
    {'key': 'Segment A', 'name': 'seg 1', 'description': 'Test segment 1'},
    {'key': 'Segment B', 'name': 'seg 2', 'description': 'Test segment 2'}
]


def test_create_segment(db_session):
    segment_in = SegmentCreate(**data[0])
    segment = create_segment(db_session, segment_in)
    assert isinstance(segment, Segment)
    assert segment.key == data[0]['key']


def test_get_segment(db_session):
    segment_in = SegmentCreate(**data[0])
    segment = create_segment(db_session, segment_in)
    fetched = get_segment(db_session, segment.id)
    assert fetched.id == segment.id


def test_get_segments(db_session):
    create_segment(db_session, SegmentCreate(**data[0]))
    create_segment(db_session, SegmentCreate(**data[1]))
    segments = get_segments(db_session)
    assert len(segments) == 2


def test_update_segment(db_session):
    created = create_segment(db_session, SegmentCreate(**data[0]))
    updated = update_segment(db_session, created.id,
                             SegmentUpdate(key='Updated Z'))
    assert updated.key == 'Updated Z'
    assert updated.description == data[0]['description']


def test_delete_segment(db_session):
    created = create_segment(db_session, SegmentCreate(**data[0]))
    deleted_result = delete_segment(db_session, created.id)
    assert deleted_result['ok'] == True
    assert len(get_segments(db_session)) == 0
